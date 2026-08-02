from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

phone_validators=RegexValidator(
    regex=r"^09\d{9}$" ,
    message="phone number must be in 09********* format"
)
class User(AbstractUser):
    
    CUSTOMER='customer'
    PROVIDER='provider'
    ROLE_CHOICE=[
        (CUSTOMER,'customer'),
        (PROVIDER,'provider')
    ]


    phone_number=models.CharField(
    max_length=11,
    unique=True ,
    validators=[phone_validators]
    )

    role=models.CharField(
        max_length=10,
        choices=ROLE_CHOICE,
        default=CUSTOMER

    )


    def __str__(self):
        return self.phone_number | self.username

