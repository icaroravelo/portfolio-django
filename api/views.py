from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testPageView(request):
    return render(request, 'test/test.html')

def homePageView(request):
    return render(request, 'home/home.html')