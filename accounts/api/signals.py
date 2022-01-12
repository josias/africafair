from af.settings.base import AUTH_USER_MODEL, ANONYMOUS_USER_NAME
from django.contrib.auth.models import Permission, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

from accounts.models import UserProfile


@receiver(post_save, sender=AUTH_USER_MODEL, dispatch_uid='create_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile instance for all newly created User instances. We only
    run on user creation to avoid having to check for existence on each call
    to User.save.
    """
    #user, created = kwargs["instance"], kwargs["created"]
    user=instance
    if created and user.email != ANONYMOUS_USER_NAME:
        profile = UserProfile.objects.create(user=user)
        # assign_perm('accounts.view_userprofile', user, profile)
        # assign_perm('accounts.change_userprofile', user, profile)
        # can_view_profile = Permission.objects.get(codename='view_userprofile')
        # user.user_permissions.add(can_view_profile)
        visitors = Group.objects.filter(name='visitors')
        user.groups.add(visitors[0])