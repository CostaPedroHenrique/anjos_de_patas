__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"

from django.db import models
from pets.models import Pet

class adocao(models.Model):
    pet = models.ForeignKey(
        Pet,
        verbose_name='Pet',
        on_delete=models.SET_NULL
    )

    candidato = models.CharField(
        verbose_name='Candidato',
        max_length=60,
    )

    candidato_contato = models.CharField(
        verbose_name='Número do Candidato',
        max_length=25
    )

    contato_whatsapp = models.CharField(
        verbose_name='Whatsapp do Candidato',
        max_length=25
    )

    finalizada = models.BooleanField(
        verbose_name='Finalizada',
        default=False,

    )


    def __str__(self):
        return "Solicitação #{}".format(self.id)

    class Meta:
        app_label = "adocoes"
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'