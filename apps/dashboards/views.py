from django.shortcuts import render , redirect
from django.contrib.auth.decorators import  login_required

def cusstomer_dashboard(request):
    pass


@login_required
def provider_dashboard(request):

