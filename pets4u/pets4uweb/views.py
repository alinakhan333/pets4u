from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic 
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView 
from django_filters import FilterSet

from .models import Pet
from .tables import PetTable

# Create your views here.
class PetFilter(FilterSet):
    class Meta:
        model = Pet
        fields = {"name": ["exact", "contains"], "age": ["exact"]}
class PetList(SingleTableMixin, FilterView):
    model = Pet 
    table_class = PetTable
    template_name = "pet_list.html"

    filterset_class = PetFilter

class DetailView(generic.DetailView):
    model = Pet
    template_name = "pets4uweb/detail.html"

