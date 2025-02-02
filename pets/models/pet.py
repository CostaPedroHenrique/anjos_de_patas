__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"

from django.db import models


class Pet(models.Model):
    OPCOES_PETS = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
    )

    nome = models.CharField(
        verbose_name="Nome",
        max_length=60,
        choices=OPCOES_PETS,
        blank=True, null=True,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        blank=True, null=True,
    )

    ativo = models.BooleanField(
        verbose_name="Ativo",
        default=False,
    )


    adotado = models.BooleanField(
        verbose_name="Adotado",
        default=False,
    )

    cidade = models.CharField(
        verbose_name="Cidade",
        max_length=80,
        blank=True, null=True,
    )

    uf = models.CharField(
        verbose_name="UF",
        max_length=4,
        blank=True, null=True,
    )

    contato = models.CharField(
        verbose_name="Contato",
        max_length=25,
        blank=True, null=True,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pets"
        verbose_name = "Pet"
        verbose_name_plural = "Pets"