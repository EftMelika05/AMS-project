from django.shortcuts import render , redirect
from .forms import RegisterForm ,LoginForm , ResetpassForm
from .models.user import User
from .models.customer_profile import CustomerProfile
from .models.provider_profile import ProviderProfile
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout


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

    if request.method=="POST":

        form=LoginForm(request.POST)

        if form.is_valid :

            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            user=authenticate(
                request ,
                username=username , 
                password=password
            )

            if user is not None:

                login(request, user)

                if user.role==User.CUSTOMER:
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

                form.add_error(
                    None ,
                    "username or password is incorrect"
                )

                
    else:

        form=LoginForm()

    return render(
        request ,
        "accounts/login.html" ,
        { 
          "form":form
        }
    )

def logout_view(request):

    logout(request)

    return redirect("login")


def resetpassword_view(request):

    if request.methood == "POST" :

        form=ResetpassForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            user=form.save(commit=False)

            new_password=form.cleaned_data["new_password"]
            user.set_password(new_password)

            user.save()



    else:
