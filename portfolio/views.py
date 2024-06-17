from django.shortcuts import render

# Create your views here.
def categoriesPage(request):
    return render(request, 'portfolio/categories.html')