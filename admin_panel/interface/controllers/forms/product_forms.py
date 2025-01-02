from django import forms

from shop.infrastructure.orm.models import Product
from core.interface.constants import FIELD_STYLE


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'discount', 'stock', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                **FIELD_STYLE,
            }),
            'price': forms.NumberInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter product price'
            }),
            'discount': forms.NumberInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter discount percentage'
            }),
            'stock': forms.NumberInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter available stock'
            }),
            'image': forms.ClearableFileInput(attrs={
                **FIELD_STYLE,
            }),
            'description': forms.Textarea(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter product description'
            }),
        }



class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'discount', 'stock', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                **FIELD_STYLE,
            }),
            'price': forms.NumberInput(attrs={
                **FIELD_STYLE,
            }),
            'discount': forms.NumberInput(attrs={
                **FIELD_STYLE,
            }),
            'stock': forms.NumberInput(attrs={
                **FIELD_STYLE,
            }),
            'image': forms.ClearableFileInput(attrs={
                **FIELD_STYLE,
            }),
            'description': forms.Textarea(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter product description'
            }),
        }

