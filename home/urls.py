from django.urls import path
from .views import(
    index,
    sobre,
    veterinarios,
    contato
)

urlpatterns = [
    path('', index, name="index"),
    path('/sobre', sobre, name="sobre"),
    path('/veterinarios', veterinarios, name="veterinarios"),
    path('/contato', contato, name="contato"),
]