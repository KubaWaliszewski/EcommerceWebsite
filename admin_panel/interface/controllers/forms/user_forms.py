from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from core.interface.constants import FIELD_STYLE


User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs=FIELD_STYLE)
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'password'] 
        widgets = {
            'first_name': forms.TextInput(attrs=FIELD_STYLE),
            'last_name': forms.TextInput(attrs=FIELD_STYLE),
            'email': forms.EmailInput(attrs=FIELD_STYLE),
            'role': forms.Select(attrs=FIELD_STYLE),
        }

    def save(self, commit=True):

        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'is_active'] 
        widgets = {
            'first_name': forms.TextInput(attrs=FIELD_STYLE),
            'last_name': forms.TextInput(attrs=FIELD_STYLE),
            'email': forms.EmailInput(attrs=FIELD_STYLE),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-6 h-6 mr-2 align-middle border-gray-300 rounded cursor-pointer'
            }),
            'role': forms.Select(attrs=FIELD_STYLE),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    