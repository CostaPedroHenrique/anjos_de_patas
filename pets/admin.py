from django.contrib import admin
from .models import( 
    Pet,
    Foto,
)


class FotoInline(admin.StackedInline):
    model = Foto
    fields = ['foto']

    extra = 0

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_nascimento', 'adotado']
    inlines = [FotoInline]

