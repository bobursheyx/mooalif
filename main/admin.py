# admin.py
from django.contrib import admin
from .models import Ariza

@admin.register(Ariza)
class ArizaAdmin(admin.ModelAdmin):
    list_display = ('ismi', 'email', 'telefon_nomer', 'xabar')
    fields = ('ismi', 'email', 'telefon_nomer', 'xabar')
