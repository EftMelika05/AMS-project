from django import forms
from  apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.core.exceptions import ValidationError


class ProviderProfileForm(forms.ModelForm):

    class Meta:

       model=ProviderProfile

       fields=[
          "full_name" ,
          "province" ,
          "city" ,
          "gender" ,
          "profie_image" ,
          "Specialities" ,
          "bio" ,
          "experience"

        ]
