from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.user import User
from .models.customer_profile import CustomerProfile
from .models.provider_profile import ProviderProfile
from .models.provider_profile import Speciality

@admin.register(User)
class customUserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(
        (
           'Extra info',
           {
                'fields': (
                  'phone_number',
                 'role',
                )
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Extra info',
            {
                'fields': (
                    'phone_number',
                    'role',
                )
            }
        ),
    )

admin.site.register(CustomerProfile)

admin.site.register(ProviderProfile)

admin.site.register(Speciality)