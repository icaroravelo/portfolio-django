from django.shortcuts import render, redirect
from django.http import HttpResponse

import cloudinary.uploader

from about.views import aboutPage
from portfolio.views import categoriesPage, individualCategoryPage
from school.views import schoolPage
from contact.views import contactPage
from blog.views import blogHomePage 

from about.models import About, Stack, Experience

# Create your views here.
def testPageView(request):
    return render(request, 'test/test.html')

def homePageView(request):
    infos = About.objects.all() # Fetch all about data from database
    stacks = Stack.objects.all() # Fetch all stack data from database
    experiences = Experience.objects.all() # Fetch all experience data from database
    context = {
        'infos': infos,
        'stacks': stacks,
        'experiences': experiences
    }
    return render(request, 'home/home.html', context)

def errorPageView(request):
    return redirect(request, '404/404.html')

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
