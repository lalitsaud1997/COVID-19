from django.contrib import admin
from .models import Coronavirus

# Register your models here.

class CoronavirusAdmin(admin.ModelAdmin):
    list_display = ['country','total_cases','total_deaths','total_recovered']
    search_fields = ['country']
    ordering = ['-total_cases',]

admin.site.register(Coronavirus, CoronavirusAdmin)
