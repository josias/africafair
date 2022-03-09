from operator import mod
from re import I
from statistics import mode
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from fair_sites.models import Site, Quarter, Zone, Town, Department, Country
from fair_sites.resources import SiteResource, QuarterResource, ZoneResource, TownResource, DepartmentResource, CountryResource


class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

admin.site.register(Country, CountryAdmin)


class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource

admin.site.register(Department, DepartmentAdmin)


class TownAdmin(ImportExportModelAdmin):
    resource_class = TownResource
    search_fields = ['name',]
    list_display = ('name', 'department')
    list_filter = ['department',]
admin.site.register(Town, TownAdmin)


class ZoneAdmin(ImportExportModelAdmin):
    resource_class = ZoneResource
    search_fields = ['name',]
    list_display = ('name', 'town')
    list_filter = ['town__department', 'town']

admin.site.register(Zone, ZoneAdmin)


class QuarterAdmin(ImportExportModelAdmin):
    resource_class = QuarterResource
    search_fields = ['name',]
    list_display = ('name', 'zone')
    list_filter = ['zone__town', 'zone', ]

admin.site.register(Quarter, QuarterAdmin)


class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResource

admin.site.register(Site, SiteAdmin)

""" class SiteInline(admin.StackedInline):
    model = Site

class QuarterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [SiteInline,]
    extra_fields = 1 


admin.site.register(Quarter, QuarterAdmin)"""

