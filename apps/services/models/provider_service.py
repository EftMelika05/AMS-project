from django.db import models
from apps.accounts.models.provider_profile import ProviderProfile
from .service_type import ServiceType

class ProviderService(models.Model):

    provider=models.ForeignKey(
        ProviderProfile,
        related_name='provider_service',
        on_delete=models.CASCADE
    )

    service_type=models.ForeignKey(
        ServiceType,
        related_name='provider_service',
        on_delete=models.CASCADE
    )

    title=models.CharField(max_length=100 , blank=True , null=True)

    description=models.TextField(blank=True)

    main_image=models.ImageField(
        upload_to='provider_service/',
        blank=True
    )

    price=models.PositiveBigIntegerField(help_text="قیمت هر سرویس")

    duration=models.PositiveIntegerField(help_text='مدت زمان سرویس به دقیقه')

    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.provider} | {self.service_type}"


