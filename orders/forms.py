from django import forms

from .models import Order
from core.constants import FIELD_STYLE


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address', 'address2', 'city', 'zip_code', 'country', 'phone',)
        widgets = {
            'full_name': forms.TextInput(attrs=FIELD_STYLE),

            'address': forms.TextInput(attrs=FIELD_STYLE),        
            'address2': forms.TextInput(attrs=FIELD_STYLE),        
            'city': forms.TextInput(attrs=FIELD_STYLE),        
            'zip_code': forms.TextInput(attrs=FIELD_STYLE),        
            'country': forms.TextInput(attrs=FIELD_STYLE),        
            'phone': forms.TextInput(attrs=FIELD_STYLE),        
        }