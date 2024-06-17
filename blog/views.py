from django.shortcuts import render

# Create your views here.
def blogHomePage(request):
    return render(request, 'blog/main.html')