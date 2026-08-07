from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import provider_required
from apps.services.forms.provider_service_form import ProviderServiceForm
from apps.services.models.provider_service import ProviderService
from django.contrib import messages

@login_required
@provider_required
def CreateService_view(request):

    if request.method=="POST":

        form=ProviderServiceForm(
            request.POST ,
            request.FILES
        )


        if form.is_valid():

            provider=request.user.provider_profile

            if not provider.is_verified :

                messages.error(
                     "Your account has not been verified yet."
                )
                return redirect("provider_dashboard")
            
            
            if not provider.specialities.exists() :

                messages.error(
                     "Complete your specialities first."
                )
                return redirect("provider_profile")


            duplicate=ProviderService.objects.filter(
                provider=provider ,
                title=form.cleaned_data["title"]
            ).exists()

            if duplicate :

                form.add_error(
                    "title" , 
                    "this service has already been created."
                )
            else:

              service=form.save(commit=False)
 
              service.provider=provider

              service.save()

              messages.success(
                  request, 
                  "service created successfully"
                )
              return redirect("provider_dashboard")

    else:

        form=ProviderServiceForm()


    return render(
        request ,
        "services/create_service.html",
        {
            "form":form
        }
    )


    