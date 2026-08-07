from django.shortcuts import render , redirect
from django.contrib.auth.decorators import  login_required
from apps.accounts.decorators import customer_required , provider_required

@customer_required
@login_required
def CustomerDashboard_view(request):
    return render(
        request ,
        "dashboard/customer_dashboard.html"
    )


@provider_required
@login_required
def ProviderDashboard_view(request):
    return render(
        request ,
        "dashboard/provider_dashboard.html"
    )

