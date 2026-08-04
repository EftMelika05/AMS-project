from django import forms
from  apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    confirm_password=forms.CharField()

    class Meta:
        model=User

        fields=[
            "username",
            "phone_number",
            "role",
            "password"
        ]

    def clean(self):

        cleaned_data=super().clean()

        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")

        if password and confirm_password :

            if password != confirm_password :
                    
                raise forms.ValidationError(
                    "passwords do not match"
                )

        return cleaned_data

    



class CustomerProfileForm(forms.ModelForm):

    class Meta:

        model=CustomerProfile

        fields=[
            "full_name" ,
            "gender" ,
            "province" ,
            "city" 
        ]


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
