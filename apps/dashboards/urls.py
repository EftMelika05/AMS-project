from django.urls import path
from . import views

urlpatterns=[
    path('customer/dashboard', views.cusstomer_dashboard , name="customer_dashboard"),
    path("provider/dashboard" , views.provider_dashboard , name="provider_dashboard"),
]