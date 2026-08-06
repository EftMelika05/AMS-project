from django.shortcuts import render , redirect
from apps.accounts.forms.provider_profile_form import ProviderProfileForm
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import provider_required


@provider_required
@login_required
def ProviderProfile_view(request):
    if request.method=='POST':

        form=ProviderProfileForm(
            request.POST ,
            request.FILES ,
            instance=request.user.provider_profile
        )

        if form.is_valid():

            form.save()

            return redirect("provider_profile")


    else:

        form=ProviderProfileForm(
            instance=request.user.provider_profile
        )

    return render(
        request , 
        "accounts/provider_profile.html" ,
        {
            "form":form
        }
    )
