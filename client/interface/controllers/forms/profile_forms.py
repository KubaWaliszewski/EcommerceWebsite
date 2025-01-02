from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from account.infrastructure.orm.models import CustomUser
from core.interface.constants import FIELD_STYLE


class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)
        exclude = ('password1', 'password2',)
        widgets = {
            'email': forms.TextInput(attrs=FIELD_STYLE),
            'first_name': forms.TextInput(attrs=FIELD_STYLE),
            'last_name': forms.TextInput(attrs=FIELD_STYLE),
        }


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs=FIELD_STYLE),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=FIELD_STYLE),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=FIELD_STYLE),
        label="Confirm New Password"
    )

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')
        