from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    CUSTOMER='customer'
    PROVIDER='provider'
    ROLE_CHOICE=[
        (CUSTOMER,'customer'),
        (PROVIDER,'provider')
    ]


    phone_number=models.CharField(
    max_length=11,
    unique=True
    )

    role=models.CharField(
        max_length=10,
        choices=ROLE_CHOICE,
        default=CUSTOMER

    )


    def __str__(self):
        return self.username

