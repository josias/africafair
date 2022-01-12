from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField
from phonenumber_field.modelfields import PhoneNumberField

from af.core.models import TimestampModel
from af.settings.base import AUTH_USER_MODEL
from fair_sites.models import Site


class Business(TimestampModel):
    full_name = models.CharField(verbose_name=_('full_name'), max_length=250)
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        limit_choices_to={'is_active':True, 'groups__name':'owner'},
        blank=True, null=True
    )
    logo = VersatileImageField(
        'logo',
        upload_to='business_logos/',
        ppoi_field='logo_ppoi', 
        blank=True, 
        null=True,
    )
    logo_ppoi = PPOIField(blank=True, null=True)

    # Methods
    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name', 'created_at' ]
        verbose_name = _('business')
        verbose_name_plural = _('businesses')


class Shop(TimestampModel):
    short_name = models.CharField(verbose_name=_('short_name'), max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='point_of_sales')
    is_headquater = models.BooleanField(verbose_name=_('is headquater'), default=True)
    seller = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        limit_choices_to={'is_active':True, 'groups__name':'seller'},
        related_name='shops',
        blank=True,
        null=True
    )
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='shops')
    whatsapp = PhoneNumberField(unique = True, null = False, blank = False)
    bonus_rate = models.DecimalField(verbose_name=_('bonus rate'), decimal_places=2, max_digits=5, null=True)
    
    # Methods
    def set_bonus_rate(self, **kwargs):
        self.bonus_rate = kwargs['rate']
        return self.bonus_rate

    def __str__(self):
        return f"{self.short_name} of {self.site}"

    class Meta:
        ordering = ['short_name', 'created_at' ]
        verbose_name = _('shop')
        verbose_name_plural = _('shops')
