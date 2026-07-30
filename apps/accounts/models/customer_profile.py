from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerProfile(models.Model):
    
    MALE='male'
    FEMALE='female'
    GENDER_CHOISE=(
        ( MALE,'male'),
        ( FEMALE , 'female')
    )


    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile'
    )

    full_name=models.CharField(max_length=100)

    gender=models.CharField(
        max_length=10,
        choices=GENDER_CHOISE,
        blank=True
    )

    province=models.CharField(max_length=50)

    city=models.CharField(max_length=50)


    def __str__(self):
        return self.full_name



    

