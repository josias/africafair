from django.contrib import admin
from accounts.models import UserProfile, CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from guardian.admin import GuardedModelAdmin
from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(GuardedModelAdmin):
    
    model = UserProfile
    list_display = ('user', 'id', 'language_preference')
    
    

UserProfileAdmin.user_can_access_owned_objects_only = False    
UserProfileAdmin.user_can_access_owned_by_group_objects_only = True

""" add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserProfile
    list_display = ('id', 'language_preference')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    ) """


admin.site.register(UserProfile, UserProfileAdmin)