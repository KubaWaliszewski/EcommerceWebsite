from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class CreateUserForm(UserCreationForm, forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border mb-6'}),
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border mb-6'}),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
        }


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            'placeholder': 'Enter your password'
        })
    )

