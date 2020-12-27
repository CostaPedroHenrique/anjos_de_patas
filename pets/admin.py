from django.contrib import admin
from .models.pet import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_nascimento', 'adotado']
