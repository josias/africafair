from django.db import models
from django.utils.translation import gettext_lazy as _
# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from core.models import TimestampModel


class Region(TimestampModel):
    name = models.CharField(verbose_name='nom', max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    # Methods
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name


class Pays(Region):

    class Meta(Region.Meta):
        verbose_name = 'pays'
        verbose_name_plural = 'pays'


class Ville(Region):
    pays = models.ForeignKey(Pays,  on_delete=models.CASCADE)

    class Meta(Region.Meta):
        verbose_name = 'ville'
        verbose_name_plural = 'villes'


class Zone(Region):
    ville = models.ForeignKey(Ville,  on_delete=models.CASCADE)

    class Meta(Region.Meta):
        verbose_name = 'zone'
        verbose_name_plural = 'zones'


class Quartier(Region):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta(Region.Meta):
        verbose_name = 'quartier'
        verbose_name_plural = 'quartiers'


class Site(TimestampModel):
    site_code = models.CharField(verbose_name="code du site", max_length=50)
    quartier = models.ForeignKey(Quartier,  on_delete=models.CASCADE)
    name = models.CharField(verbose_name='nom', max_length=50,)
    address = models.CharField(verbose_name='adresse', max_length=100, null=True, blank=True)

    # Methods
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]
        verbose_name = 'site'
        verbose_name_plural = 'sites'

