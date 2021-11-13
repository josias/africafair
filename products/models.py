from re import I
from django.db import models
from af.core.models import TimestampModel
from af.settings.base import AUTH_USER_MODEL


class Product(TimestampModel):
    name = models.CharField(verbose_name=('name'), max_length=50)
    description = models.CharField(verbose_name=('description'), max_length=200,)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name
