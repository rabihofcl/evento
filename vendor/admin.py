from django.contrib import admin
from .models import Vendor, VendorSubscription
# Register your models here.


admin.site.register(Vendor)
admin.site.register(VendorSubscription)