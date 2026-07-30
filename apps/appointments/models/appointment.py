from django.db import models
from apps.accounts.models.customer_profile import CustomerProfile
from apps.services.models.provider_service import ProviderService
from django.core.exceptions import ValidationError


class Appointment(models.Model):

    customer=models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    provider_service=models.ForeignKey(
       ProviderService,
       on_delete=models.CASCADE,
       related_name='appointments'
    )

    date=models.DateField()

    start_time=models.TimeField()
    end_time=models.TimeField()

    def clean(self):
       if self.end_time <= self.start_time :
          raise ValidationError({
             "end_time":"end_time must be after start-time"
          })    

    PENDING='pending'
    CONFIRMED='confirmed'
    DONE='done'
    CANCELLED='cancelled'
    STATUS_CHOICES=[
        (PENDING,'pending'),
        (CONFIRMED,'confirmed'),
        (DONE,'done'),
        (CANCELLED,'cancelled')
    ]

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.full_name} | {self.provider_service} | {self.date} | {self.start_time}"
