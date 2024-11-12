# from django import forms
# from django.contrib.auth.forms import PasswordChangeForm

# from .models import Address
# from account.models import CustomUser


# class UpdateUserForm(forms.ModelForm):

#     password = None

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name',)
#         exclude = ('password1', 'password2',)
#         widgets = {
#             'email': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'first_name': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#         }

# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ('first_name', 'last_name', 'address', 'address2', 'city', 'zip_code', 'country', 'phone',)
#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'address': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'address2': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'city': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'zip_code': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'country': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#             'phone': forms.TextInput(attrs={
#                 'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#             }),
#         }


# class ChangePasswordForm(PasswordChangeForm):

#     old_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#         }),
#         label="Old Password"
#     )
#     new_password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#         }),
#         label="New Password"
#     )
#     new_password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'w-full py-4 px-6 rounded-xl border mb-6'
#         }),
#         label="Confirm New Password"
#     )

#     class Meta:
#         model = CustomUser
#         fields = ('old_password', 'new_password1', 'new_password2')
        