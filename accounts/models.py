from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from af.core.models import TimestampModel
from accounts.managers import CustomUserManager
from af.settings.base import AUTH_USER_MODEL
from guardian.mixins import GuardianUserMixin

import uuid


def get_anonymous_user_instance(User):
    if User.objects.filter(email='anonymous@af.com').exists():
        return 1
    else:
        return User(first_name= 'John', last_name='Doe', email='anonymous@af.com', password='12345678')


class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  VISITOR = 1
  CUSTOMER = 2
  SELLER = 3
  OWNER = 4
  EDITOR = 5
  ROLE_CHOICES = (
      (VISITOR, 'visitor'),
      (CUSTOMER,'customer'),
      (SELLER, 'seller'),
      (OWNER, 'owner'),
      (EDITOR,'editor')
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class CustomUser(AbstractBaseUser, PermissionsMixin, GuardianUserMixin):
    roles = models.ManyToManyField(Role)
    username_validator = ASCIIUsernameValidator()

    """username = CICharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )"""
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = CIEmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(TimestampModel):
    """This model stores all information relative to a user which doesn't belong to
    authentication."""

    FRENCH = 'FR'
    ENGLISH = 'EN'
    LANGUAGE_CHOICE = [
        (FRENCH, 'français'),
        (ENGLISH, 'english'),
    ] 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(AUTH_USER_MODEL,
                                on_delete=models.CASCADE, 
                                related_name='profile')
    
    language_preference = models.CharField(max_length=2,
                                           choices=LANGUAGE_CHOICE,
                                           default=ENGLISH)
    def __str__(self):
        return self.user.username
    class Meta:
        permissions = (
            #('view_userprofile', 'View UserProfile'),
        )
