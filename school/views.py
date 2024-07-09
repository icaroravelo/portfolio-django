from django.shortcuts import render, redirect
from .models import School

# Create your views here.
def schoolPage(request, order_by='finished_at'):
    schools = School.objects.all().order_by(order_by) 
    context = {
        'schools': schools,
    }
    return render(request, 'school/school.html', context)

def certificatePage(request):
    certificates = School.objects.all()
    context = {
        'certificates': certificates
    }
    return redirect(request, context)