from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from shop.models import Product, Category

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl border mb-6'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'password'] 
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
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
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-6 h-6 mr-2 align-middle border-gray-300 rounded cursor-pointer'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    

# ===============================
# Products Management Forms
# ===============================


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'discount', 'stock', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter product price'
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter discount percentage'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter available stock'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter product description'
            }),
        }



class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'discount', 'stock', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter product description'
            }),
        }



class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6',
                'placeholder': 'Enter category name'
            })
        }


