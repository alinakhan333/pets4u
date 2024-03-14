from django.urls import path

from . import views
from .views import display_pets

urlpatterns = [
    path("display_pets/", display_pets, name="display_pets"),
]