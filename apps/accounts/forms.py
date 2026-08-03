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
