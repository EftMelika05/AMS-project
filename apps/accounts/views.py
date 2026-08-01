from django.shortcuts import render
from django.shortcuts import render

def login_view(request):
    return render(request , "accounts/login.html")



