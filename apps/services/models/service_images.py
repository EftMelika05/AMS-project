from django.db import models
from .provider_service import ProviderService

class ServiceImages(models.Model):

    service=models.ForeignKey(
        ProviderService,
        on_delete=models.CASCADE,
        related_name='images'
    )

    img=models.ImageField(
        upload_to='service_images/',
        blank=True
    )

    description=models.TextField(blank=True , null=True)


    def __str__(self):
        return f"images | {self.service}"