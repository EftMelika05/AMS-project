from django import forms
from .models.user import User
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


