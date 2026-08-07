from django.shortcuts import render , redirect
from apps.accounts.forms.customer_profile_form import CustomerProfileForm
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import customer_required


@login_required
@customer_required
def CustomerProfile_view(request):

 if request.method=="POST":

   form=CustomerProfileForm(
     request.POST ,
     instance=request.user.customer_profile
   )

   if form.is_valid():
      
      form.save()

      return redirect("customer_profile") 
  
 else:
   
   form=CustomerProfileForm(
     instance=request.user.customer_profile
   )

 return render(
      request , 
     "accounts/customer_profile.html",
     {
       "form":form
     }
  )