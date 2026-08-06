from django.urls import path
from .views import auth , customer_profile , provider_profile

urlpatterns=[
    path("login/", auth.login_view , name='login'),
    path("register/", auth.register_view , name="register") ,
    path("customer_profile/" , customer_profile.CustomerProfile_view , name="customer_profile") ,
    path("provider_profile/" , provider_profile.ProviderProfile_view, name="provider_profile")
]