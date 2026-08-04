from django.shortcuts import render , redirect
from apps.accounts.forms import RegisterForm ,LoginForm , ResetpassForm
from apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout


def CustomerProfile_view(request):
