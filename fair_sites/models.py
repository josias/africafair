from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
# Cette fonction est utilisée pour formater les URL
from django.urls import reverse
from af.core.models import TimestampModel


class Region(TimestampModel):
    name = models.CharField(verbose_name=_('name'), max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    # Methods
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name


class Country(TimestampModel):
    name = CountryField()

     # Methods
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('country-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class Department(Region):
    country= models.ForeignKey(Country, on_delete=models.CASCADE, related_name='departments')

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.pk})

    class Meta(Region.Meta):
        verbose_name = _('department')
        verbose_name_plural = _('departments')


class Town(Region):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='towns')

    def get_absolute_url(self):
        return reverse('town-detail', kwargs={'pk': self.pk})

    class Meta(Region.Meta):
        verbose_name = _('town')
        verbose_name_plural = _('towns')


class Zone(Region):
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='zones')

    def get_absolute_url(self):
        return reverse('zone-detail', kwargs={'pk': self.pk})

    class Meta(Region.Meta):
        verbose_name = _('zone')
        verbose_name_plural = _('zones')


class Quarter(Region):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='quaters')
    
    def get_absolute_url(self):
        return reverse('quarter-detail', kwargs={'pk': self.pk})

    class Meta(Region.Meta):
        verbose_name = _('quarter')
        verbose_name_plural = _('quarters')


class Site(TimestampModel):
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='sites')
    street = models.CharField(verbose_name=_('street'), max_length=50, default='anywhere')
    address = models.CharField(verbose_name=_('address'), max_length=100, null=True, blank=True)

    # Methods
    def __str__(self):
        return self.address

    class Meta:
        ordering = ['created_at', ]
        verbose_name = _('site')
        verbose_name_plural = _('sites')