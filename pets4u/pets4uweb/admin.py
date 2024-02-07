from django.contrib import admin

from .models import User 
from .models import Pet

admin.site.register(User)
admin.site.register(Pet)
