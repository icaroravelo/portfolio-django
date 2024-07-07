from django.shortcuts import render
from .models import About, Stack, Experience

# Create your views here.
def aboutPage(request):
    infos = About.objects.all() # Fetch all about data from database
    stacks = Stack.objects.all() # Fetch all stack data from database
    experiences = Experience.objects.all() # Fetch all experience data from database
    context = {
        'infos': infos,
        'stacks': stacks,
    }
    return render(request, 'about/about.html', context)