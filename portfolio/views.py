from django.shortcuts import render
from .models import Category

# Create your views here.
def categoriesPage(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'portfolio/categories.html', context)