__author__ = "Pedro Henrique da Costa"
__copyright__ = "Copyright 2020, Prosoft Soluções"
__credits__ = ["Prosoft Soluções"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Henrique da Costa"
__email__ = "devpedrohenrique@gmail.com"
__status__ = "Production"


from django.db import models
from .pet import Pet

class Foto(models.Model):
    foto = models.ImageField(
        verbose_name="Foto",
        upload_to='parceiros/fotos/'
    )

    pet = models.ForeignKey(
        Pet, 
        verbose_name="Pet",
        on_delete= models.CASCADE
    )
    def __str__(self):
        return "Imagem #{}".format(self.id)

    class Meta:
        app_label = "pets"
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'