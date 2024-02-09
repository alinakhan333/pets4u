from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic 
from django_tables2 import SingleTableView

from .models import Pet
from .tables import PetTable

# Create your views here.
class PetList(SingleTableView):
    model = Pet 
    table_class = PetTable
    template_name = 'pet_list.html'

class DetailView(generic.DetailView):
    model = Pet
    template_name = "pets4uweb/detail.html"

