from django.urls import path

from . import views
from .views import PetList

urlpatterns = [
    path("pets/", PetList.as_view()),
]