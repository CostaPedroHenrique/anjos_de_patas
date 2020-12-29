__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"


from django.db import models

class Duvida(models.Model):
    pergunta = models.TextField(
        verbose_name = 'Pergunta'
    )

    resposta = models.TextField(
        verbose_name = 'Resposta'
    )

    aparece_na_home = models.BooleanField(
        verbose_name = 'Aparecer na home do site?'
    )

    def __str__(self):
        return "dúvida-{}".format(self.id)

    class Meta:
        app_label = "home"
        verbose_name = "Dúvida"
        verbose_name_plural = "Dúvidas"