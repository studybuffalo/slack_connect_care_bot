"""Forms for the User app."""
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    """Form to change user model details."""
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    """Form to create new user model."""
    error_message = admin_forms.UserCreationForm.error_messages.update(
        {'duplicate_username': 'This username has already been taken.'}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        """Extending field cleaning to confirm username is unique."""
        username = self.cleaned_data['username']

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages['duplicate_username'])
