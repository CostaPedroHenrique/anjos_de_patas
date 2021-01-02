from django import forms
from .models import Contato



class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs = {'class': 'form-control',
                'placeholder': 'Nos diga seu nome'}
            ),

            'email': forms.EmailInput(
                attrs = {'class': 'form-control',
                'placeholder': 'Seu melhor E-mail para entrarmos em contato com você'}
            ),

            'assunto': forms.TextInput(
                attrs = {'class': 'form-control',
                'placeholder': 'Nos informe com uma frase o que aconteceu'}
            ),

            'mensagem': forms.Textarea(
                attrs = {'class': 'form-control',
                'placeholder': 'Por favor, agora nos diga com detalhes o ocorrido'}
            ),
        }