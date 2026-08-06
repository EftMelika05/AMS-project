from functools import wraps
from django.shortcuts import render
from apps.accounts.models.user import User
from django.core.exceptions import PermissionDenied


def customer_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != User.CUSTOMER :

            raise PermissionDenied

        return view_func(request, *args, **kwargs)
    
    return wrapper


def provider_required(view_func):

    @wraps(view_func)
    def wrapper(request , *args , **kwargs):

        if request.user.role != User.PROVIDER :
            raise PermissionDenied

        return view_func(request , *args , **kwargs)
    
    return wrapper