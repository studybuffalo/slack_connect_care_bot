"""Models for the Connect Care Bot."""
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """Default user for Connect Care Bot."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(
        blank=True,
        help_text='Name of User',
        max_length=255,
        null=True,
    )
