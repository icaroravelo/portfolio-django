from django.shortcuts import render

# Create your views here.
def schoolPage(request):
    return render(request, 'school/school.html')