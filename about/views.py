from django.shortcuts import render
from .models import About, Stack

# Create your views here.
def aboutPage(request):
    infos = About.objects.all() # Fetch all about data from database
    stacks = Stack.objects.all() # Fetch all stack data from database
    context = {
        'infos': infos,
        'stacks': stacks
    }
    return render(request, 'about/about.html', context)