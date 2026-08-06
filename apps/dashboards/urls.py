from django.urls import path
from . import views

urlpatterns=[
    path('customer/', views.cusstomer_dashboard , name="customer_dashboard"),
    path("provider/" , views.provider_dashboard , name="provider_dashboard"),
]