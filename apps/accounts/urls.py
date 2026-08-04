from django.urls import path
from .views import auth , customer_profile

urlpatterns=[
    path("login/", auth.login_view , name='login'),
    path("register/", auth.register_view , name="register") ,
    path("customer_profile/" , customer_profile.CustomerProfile_view , name="customer_profile")
]