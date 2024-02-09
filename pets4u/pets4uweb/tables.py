import django_tables2 as tables
from .models import Pet

class PetTable(tables.Table):
    class Meta:
        model = Pet
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "type", "location", "age")