from django.shortcuts import render, get_object_or_404, redirect
from api.services import upload_image
from .models import Category, Project, Contributor
import uuid

from about.models import Stack  

# Create your views here.
def categoriesPage(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'portfolio/categories.html', context)

# Get individual category
def individualCategoryPage(request, slug):
    print(f'Slug recebido: {slug}')
    category = get_object_or_404(Category, slug=slug)
    
    context = {
        'category': category,
    }
    return render(request, 'portfolio/individual-category.html', context)

# Function to upload image to cloudinary
def upload_portfolio_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['thumbnail']

        # Upload image to cloudinary
        image_url = upload_image['image']

        # Create a new project 
        project = Project(
            title=title,
            description=description,
            thumbnail=image_url,
            category=Category.objects.get(id=request.POST['category']),
            is_featured=request.POST.get('is_featured', False)
        )
        project.save() # Save into database

        # Add stacks and contributors, if necessary
        project.stacks.set(request.POST.getlist('stacks'))
        project.contributor.set(request.POST.getlist('contributor'))
        project.save()

        return redirect('portfolio')
    
    return render(request, {
        'categories': Category.objects.all(),
        'contributors': Contributor.objects.all(),
        'stacks': Stack.objects.all()
    })