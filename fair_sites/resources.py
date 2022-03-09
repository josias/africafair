#from dataclasses import fields
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Site, Quarter, Zone, Town, Department, Country


class CountryResource(resources.ModelResource):
    created_at = fields.Field(readonly=True)
    updated_at = fields.Field(readonly=True)

    class Meta:
        model = Country
        fields = ('id', 'name' )
        export_order = ['id', 'created_at', 'updated_at', 'name']
        import_id_fields = ('id',)


class DepartmentResource(resources.ModelResource):
    country = fields.Field(
        column_name = 'country',
        attribute = 'country',
        widget = ForeignKeyWidget(Country, 'name')
    )
    created_at = fields.Field(readonly=True)
    updated_at = fields.Field(readonly=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'country', )
        export_order = ['id', 'created_at', 'updated_at', 'name', 'country', ]
        import_id_fields = ('id',)


class TownResource(resources.ModelResource):
    """ department = fields.Field(
        column_name = 'department',
        attribute = 'department',
        widget = ForeignKeyWidget(Department, 'name')
    )
    created_at = fields.Field(readonly=True)
    updated_at = fields.Field(readonly=True)
 """
    class Meta:
        model = Town
        fields = ('id', 'name', 'department', )
        export_order = ['id', 'name', 'department', ]
        import_id_fields = ('id',)


class ZoneResource(resources.ModelResource):
   
    class Meta:
        model = Zone
        fields = ('id', 'name', 'town', )
        export_order = ['id', 'name', 'town']
        import_id_fields = ('id',)


class QuarterResource(resources.ModelResource):
    
    class Meta:
        model = Quarter
        fields = ('id', 'name', 'zone', )
        export_order = ['id', 'name', 'zone', ]
        import_id_fields = ('id',)
    


class SiteResource(resources.ModelResource):
    quarter = fields.Field(
        column_name = 'quarter',
        attribute = 'quarter',
        widget = ForeignKeyWidget(Quarter, 'name')
    )
    #created_at = fields.Field(readonly=True)
    #updated_at = fields.Field(readonly=True)

    class Meta:
        model = Site
        fields = ('id', 'street', 'address', 'quarter', )
        export_order = ['id', 'created_at', 'updated_at', 'street', 'address', 'quarter', ]
        import_id_fields = ('id',)






