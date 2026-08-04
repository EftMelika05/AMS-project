from django.shortcuts import render , redirect
from apps.accounts.forms.register_form import RegisterForm
from apps.accounts.forms.login_form import LoginForm
from apps.accounts.forms.customer_profile_form import CustomerProfileForm
from apps.accounts.forms.provider_profile_form import ProviderProfileForm
from apps.accounts.models.user import User
from apps.accounts.models.customer_profile import CustomerProfile
from apps.accounts.models.provider_profile import ProviderProfile
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout