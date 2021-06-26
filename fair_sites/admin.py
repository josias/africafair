from django.contrib import admin
from .models import Site, Quartier, Zone, Ville, Pays


class PaysAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Pays, PaysAdmin)


class VilleAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'pays']


admin.site.register(Ville, VilleAdmin)


class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'ville']


admin.site.register(Zone, ZoneAdmin)


class QuartierAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'zone']


admin.site.register(Quartier, QuartierAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'quartier']


admin.site.register(Site, SiteAdmin)

