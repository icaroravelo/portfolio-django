from django.shortcuts import render
from django.http import HttpResponse

from about.views import aboutPage
from portfolio.views import categoriesPage, individualCategoryPage
from school.views import schoolPage
from contact.views import contactPage
from blog.views import blogHomePage

from about.models import About, Stack

# Create your views here.
def testPageView(request):
    return render(request, 'test/test.html')

def homePageView(request):
    infos = About.objects.all() # Fetch all about data from database
    stacks = Stack.objects.all() # Fetch all stack data from database
    context = {
        'infos': infos,
        'stacks': stacks
    }
    return render(request, 'home/home.html', context)

def aboutPageView(request):
    return aboutPage(request)

def categoriesPageView(request):
    return categoriesPage(request)

def individualCategoryPageView(request, slug):
    return individualCategoryPage(request, slug)

def schoolPageView(request):
    return schoolPage(request)

def contactPageView(request):
    return contactPage(request)

def blogHomePageView(request):
    return blogHomePage(request)