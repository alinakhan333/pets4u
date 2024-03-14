from django.shortcuts import render

from .models import Pet

# Create your views here.
def display_pets(request):
    Pets = Pet.objects.all()
    return render (request, 'pets4uweb/display_pets.html', {'Pets': Pets})



