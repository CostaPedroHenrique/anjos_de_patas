from django.contrib import admin
from .models import ComoFunciona
from .models import Contato
from .models import Testemunho
from .models import Parceiro
from .models import Duvida
# Register your models here.



@admin.register(ComoFunciona)
class ComoFuncionaAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'comentario',
        'icone'
    ]

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'comentario',
        'foto',
        'link'
    ]

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'comentario',
        'foto',
        'aparece_na_home'
    ]


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_criacao']



@admin.register(Duvida)
class DuvidaAdmin(admin.ModelAdmin):
    fields = ['pergunta', 'resposta', 'aparece_na_home']
    list_display = ['pergunta', 'resposta', 'aparece_na_home']
