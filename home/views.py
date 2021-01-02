from django.shortcuts import render, redirect
from .models import (
    ComoFunciona,
    Contato,
    Duvida,
    Parceiro,
    Testemunho
)

from pets.models import Pet

from .forms import ContatoForm

cidade = None

def index(request):
    global cidade

    if request.method == 'POST':
        cidade = request.POST.get('cidade')
        if cidade == "None":
            cidade = None

    pets = Pet.objects.all()
    como_funciona = ComoFunciona.objects.all()
    contatos = Contato.objects.all()
    parceiros = Parceiro.objects.all()
    testemunhos = Testemunho.objects.filter(
        aparece_na_home = True
    )
    if cidade == None:
        return render(
            request,
            "cidade_index.html",
            {

            }
        )
    else: 
        return render(
            request,
            'index.html',
            {
                'pets': pets,
                'como_funciona': como_funciona,
                'contatos': contatos,
                'parceiros': parceiros,
                'testemunhos': testemunhos,
                'cidade': cidade

            }
        )


def sobre(request):
    return render(
        request,
        'sobre.html',
        {

        }
    )


def veterinarios(request):
    return render(
        request,
        'veterinarios.html',
        {
            
        }
    )


def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contato')

    return render(
        request,
        'contato.html', 
        {
            'menu': 'contato'
        }
    )