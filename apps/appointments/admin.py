from django.contrib import admin

from .models.work_schedule import WorkSchedule
from .models.schedule_exeption import ScheduleExeption
from .models.appointment import Appointment

admin.site.register(Appointment)

admin.site.register(WorkSchedule)

admin.site.register(ScheduleExeption)
