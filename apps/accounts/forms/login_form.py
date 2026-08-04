from django import forms
from  apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    username=forms.CharField(
        max_length=150
    )
    password=forms.CharField()


'''
class ResetpassForm(forms.Form):

    phone_number=forms.CharField()

    new_password=forms.CharField()
    confirm_new_password=forms.CharField()

    def clean(self):

        cleaned_data=super().clean()

        new_password=cleaned_data.get("new_password")
        confirm_new_password=cleaned_data.get("confirm_new_password")

        if new_password and confirm_new_password :
            if new_password != confirm_new_password :
                raise forms.ValidationError(
                    "passwords do not match"
                )
            
        return cleaned_data

'''
