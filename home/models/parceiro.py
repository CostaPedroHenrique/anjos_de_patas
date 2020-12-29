__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"


from django.db import models


class Parceiro(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=60
    )


    comentario = models.TextField(
        verbose_name='Comentário', 
        null=True, blank=True
    )

    foto = models.ImageField(
        verbose_name="Foto",
        upload_to='parceiros/fotos/'    
    )

    link = models.URLField(
        verbose_name='Link',
        max_length=200
    )


    def __str__(self):
        return self.nome

    class Meta:
        app_label = "home"
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'