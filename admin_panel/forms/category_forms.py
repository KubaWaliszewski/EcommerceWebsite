from django import forms

from shop.models import Category
from core.constants import FIELD_STYLE


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter category name'
            })
        }