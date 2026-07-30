from django.contrib import admin

from .models.category import Category
from .models.provider_service import ProviderService
from .models.service_images import ServiceImages
from .models.service_type import ServiceType


admin.site.register(Category)

admin.site.register(ProviderService)

admin.site.register(ServiceImages)

admin.site.register(ServiceType)
