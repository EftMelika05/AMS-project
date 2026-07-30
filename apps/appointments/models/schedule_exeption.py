from django.db import models
from apps.services.models.provider_service import ProviderService
from django.core.exceptions import ValidationError
from django.db.models import Q

class ScheduleExeption(models.Model):

    provider_service=models.ForeignKey(
       ProviderService,
       on_delete=models.CASCADE,
       related_name='schedule_exeption'
    )

    date=models.DateField(blank=True)

    start_time=models.TimeField(blank=True , null=True)
    end_time=models.TimeField(blank=True , null=True)

    def clean(self):
        
      #if just one filed fills(start_time/end-time)
        if (self.start_time is None) != (self.end_time is None):
           raise ValidationError(
               "Either fill both start and end time, or leave both empty."
           )
        
      #if all day is off
        if self.start_time is None  and  self.end_time is None :
           
            if ScheduleExeption.objects.filter(
              provider_service=self.provider_service,
              date=self.date
            ).exclude(
               pk=self.pk
            ).exists():
               raise ValidationError(
                  "an Exeption has already exist for this date."
               )
            return

        # if just a part of day is off
        if self.end_time <= self.start_time :
          raise ValidationError({
             "end_time":"end_time must be after start-time"
          })
        overlap = ScheduleExeption.objects.filter(
          provider_service=self.provider_service,
           date=self.date
        ).exclude(
          pk=self.pk
        ).filter(
          start_time__lt=self.end_time,
          end_time__gt=self.start_time
        )

        if overlap.exists():
          raise ValidationError(
             "this time frame overlaps another Exeptions"
          )


    reason=models.TextField(blank=True)

    def __str__(self):
        return f"{self.provider_service} |  {self.date} | {self.reason}"