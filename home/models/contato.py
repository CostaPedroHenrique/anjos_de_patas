__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"


from django.db import models


class Contato(models.Model):
    """
    Classe que serve para cadastrar o cliente no banco de dados quando ele faz contato conosco
    """

    nome = models.CharField(
        verbose_name = 'Nome',
        max_length = 200
    )

    email = models.EmailField(
        verbose_name = 'E-mail'
    )

    assunto = models.CharField(
        verbose_name = 'Assunto',
        max_length = 100
    )

    mensagem = models.TextField(
        verbose_name = 'Mensagem'
    )

    data_criacao = models.DateTimeField(
        verbose_name = 'Data de criação',
        auto_now_add = True
    )

    def __str__(self):
        return "{}-{}".format(self.id, self.nome)

    class Meta:
        app_label = "home"
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"