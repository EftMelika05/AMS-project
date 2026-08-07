from django import forms
from apps.services.models.provider_service import ProviderService


class ProviderServiceForm(forms.ModelForm):

    class Meta:

        model=ProviderService

        fields=[
            "service_type" ,
            "title" ,
            "description" ,
            "main_image" ,
            "price" ,
            "duration" 

        ]