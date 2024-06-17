from django.shortcuts import render
from django.http import HttpResponse

from about.views import aboutPage
from portfolio.views import categoriesPage
from school.views import schoolPage
from contact.views import contactPage
from blog.views import blogHomePage

# Create your views here.
def testPageView(request):
    return render(request, 'test/test.html')

def homePageView(request):
    return render(request, 'home/home.html')

def aboutPageView(request):
    return aboutPage(request)

def categoriesPageView(request):
    return categoriesPage(request)

def schoolPageView(request):
    return schoolPage(request)

def contactPageView(request):
    return contactPage(request)

def blogHomePageView(request):
    return blogHomePage(request)