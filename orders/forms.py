from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address', 'address2', 'city', 'zip_code', 'country', 'phone',)
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),

            'address': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
            'address2': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
            'city': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
            'zip_code': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
            'country': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
            'phone': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border mb-6'
            }),        
        }