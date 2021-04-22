from django.shortcuts import render

from .models import Profile

# Create your views here.

def homepage(request):

    profile = Profile.object.all()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)