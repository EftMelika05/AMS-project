from django.db import models
from .category import Category


class ServiceType(models.Model):

    category=models.ForeignKey(
        Category,
        related_name='service_type',
        on_delete=models.CASCADE
    )
    name=models.CharField(max_length=100)

    description=models.TextField(blank=True)

    def __str__(self):
        return f" {self.category} | {self.name}"
    