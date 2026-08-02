from django.shortcuts import render , redirect
from .forms import RegisterForm
from .models.user import User
from .models.customer_profile import CustomerProfile
from .models.provider_profile import ProviderProfile
from django.contrib import messages
def register_view(request):

    if request.method=="POST":

        form=RegisterForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            user=form.save(commit=False)

            password=form.cleaned_data["password"]
            user.set_password(password)

            user.save()

            if user.role==User.CUSTOMER :
                CustomerProfile.objects.create(
                    user=user
                )
                return redirect("customer_dashboard")
            elif user.role == User.PROVIDER :
                ProviderProfile.objects.create(
                    user=user
                )
                return redirect("provider_profile")
                

    else:
      
      form=RegisterForm()

    return render(
        request,
        "accounts/register.html",
        { 
         "form":form
        }
    )


def login_view(request):
    return render(request , "accounts/login.html")



