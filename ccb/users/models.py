"""Models for User app."""
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """Default user for Connect Care Bot."""
    name = CharField(
        blank=True,
        help_text='Name of User',
        max_length=255,
        null=True,
    )
