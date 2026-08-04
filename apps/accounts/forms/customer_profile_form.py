from django import forms
from  apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.core.exceptions import ValidationError


class CustomerProfileForm(forms.ModelForm):

    class Meta:

        model=CustomerProfile

        fields=[
            "full_name" ,
            "gender" ,
            "province" ,
            "city" 
        ]
