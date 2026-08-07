from django.urls import path
from . import views

urlpatterns=[
    path('customer/', views.CustomerDashboard_view, name="customer_dashboard"),
    path("provider/" , views.ProviderDashboard_view , name="provider_dashboard"),
]