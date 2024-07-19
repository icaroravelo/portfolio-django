from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

import cloudinary.uploader

from about.views import aboutPage
from portfolio.views import categoriesPage, individualCategoryPage
from school.views import schoolPage, certificatePage
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

def error404PageView(request, exception):
    data = {'name': 'portfolio-django-tan.vercel.app'}
    return render(request, 'error/error404.html', data)

def error500PageView(request, exception):
    data = {'name': 'portfolio-django-tan.vercel.app'}
    return render(request, 'error/error500.html')

def aboutPageView(request):
    return aboutPage(request)

def categoriesPageView(request):
    return categoriesPage(request)

def individualCategoryPageView(request, slug):
    return individualCategoryPage(request, slug)

def schoolPageView(request):
    return schoolPage(request)

def certificatePageView(request):
    return certificatePage(request)

def contactPageView(request):
    return contactPage(request)

def blogHomePageView(request):
    return blogHomePage(request)

def useTermsPageView(request):
    return render(request, 'legal/terms-of-use.html')

def privacyPolicyPageView(request):
    return render(request, 'legal/privacy-policy.html')

def cookiesPolicyPageView(request):
    return render(request, 'legal/cookies-policy.html')