from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Speciality(models.Model):

    name=models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name
    

class ProviderProfile(models.Model):
    
    MALE='male'
    FEMALE='female'
    GENDER_CHOISE=(
        ( MALE,'male'),
        ( FEMALE , 'female')
    )


    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='provider_profile'
    )

    full_name=models.CharField(max_length=100)

    province=models.CharField(max_length=50)

    city=models.CharField(max_length=50)

    gender=models.CharField(
        max_length=10,
        choices=GENDER_CHOISE,  
    )

    profie_image=models.ImageField(
        upload_to="providers/",
        blank=True,
        null=True
    )

    Specialities=models.ManyToManyField(
        Speciality,
        related_name='providers'
    )

    bio=models.TextField(
        blank=True
    )

    experience=models.PositiveBigIntegerField(
        default=0,
        help_text="سابقه کاری برحسب سال"
    )

    is_verified=models.BooleanField(
        default=False
    )
    
    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.full_name

