from django.db import models
from apps.services.models.provider_service import ProviderService
from django.core.exceptions import ValidationError
from django.db.models import Q

class WorkSchedule(models.Model):

    provider_service=models.ForeignKey(
       ProviderService,
       on_delete=models.CASCADE,
       related_name='work_schedules'
    )

    SATURDAY='saturday'
    SUNDAY='sunday'
    MONDAY='monday'
    TUESDAY='tuesday'
    WEDNESDAY='wednesday'
    THURSDAY='thursday'
    FRIDAY='friday'
    DAY_CHOICES=[
        (SATURDAY,'saturday'),
        (SUNDAY,'sunday'),
        (MONDAY,'monday'),
        (TUESDAY,'tuesday'),
        (WEDNESDAY,'wednesday'),
        (THURSDAY,'thursday'),
        (FRIDAY,'friday')
    ]

    day_of_week=models.CharField(
        max_length=40,
        choices=DAY_CHOICES
    )

    start_time=models.TimeField()
    end_time=models.TimeField()

    def clean(self):
        if self.end_time <= self.start_time :
          raise ValidationError({
             "end_time":"end_time must be after start-time"
          })
       
        overlap = WorkSchedule.objects.filter(
          provider_service=self.provider_service,
          day_of_week=self.day_of_week
        ).exclude(
          pk=self.pk
        ).filter(
          start_time__lt=self.end_time,
          end_time__gt=self.start_time
        )

        if overlap.exists():
          raise ValidationError(
             "this time frame has been already exist"
          )


    def __str__(self):
     return f"{self.provider_service} | {self.get_day_of_week_display()}"
    


