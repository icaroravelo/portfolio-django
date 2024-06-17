from django.shortcuts import render
from .models import About, Stack

# Create your views here.
def aboutPage(request):
    infos = About.objects.all()
    stacks = Stack.objects.all()
    context = {
        'infos': infos,
        'stacks': stacks
    }
    return render(request, 'about/about.html', context)