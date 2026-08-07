from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import provider_required
from apps.services.forms.provider_service_form import ProviderServiceForm
from apps.services.models.provider_service import ProviderService
from django.contrib import messages


@login_required
@provider_required
def ServiceList_view(request):

    provider=request.user.provider_profile

    services=ProviderService.objects.filter(
        provider=provider,
    )

    return render(
        request ,
        "services/service_list.html"
    )
