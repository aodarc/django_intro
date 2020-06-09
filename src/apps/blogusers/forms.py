from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    username = forms.CharField(max_length=32, validators=[validators.MinValueValidator(limit_value=4)])
    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    accept_rules = forms.BooleanField()

    def clean_accept_rules(self):
        accepted_rules = self.cleaned_data['accept_rules']
        if not accepted_rules:
            raise ValidationError(
                _('You need accept our rules'),
                code='not_accepted_rules'
            )
        return accepted_rules

    def clean_password_confirm(self):
        password = self.cleaned_data['password_confirm']
        if password != self.cleaned_data['password']:
            raise ValidationError(_("Passwords didn't match"), code='invalid_passwords')
        return password

    def clean(self):
        return self.changed_data
