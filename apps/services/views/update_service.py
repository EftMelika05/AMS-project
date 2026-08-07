from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import provider_required
from apps.services.forms.provider_service_form import ProviderServiceForm
from apps.services.models.provider_service import ProviderService
from django.contrib import messages


def UpdateService_view(request,service_id):

    provider=request.user.provider_profile
    service=ProviderService.objects.get(
        pk=service_id ,
        provider=provider
    )

    if request.methd=="POST":

        form=ProviderServiceForm(
            request.POST ,
            request.FILE ,
            instance=service
        )

        if form.is_valid():
            

    else:

        form=ProviderServiceForm(
            instance=service
        )

    return render(
        'request'
    )