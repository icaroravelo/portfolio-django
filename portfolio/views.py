from django.shortcuts import render, get_object_or_404
from .models import Category
import uuid

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