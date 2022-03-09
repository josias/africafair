from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin


from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser
from products.models import Product, Category


class CategoryAdmin(TreeAdmin, ImportExportModelAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, CategoryAdmin)


admin.site.register(Product)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('last_name',)


admin.site.register(CustomUser, CustomUserAdmin)


