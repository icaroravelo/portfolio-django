from django.shortcuts import render
from .models import School

# Create your views here.
def schoolPage(request):
    schools = School.objects.all() 
    context = {
        'schools': schools
    }
    return render(request, 'school/school.html', context)