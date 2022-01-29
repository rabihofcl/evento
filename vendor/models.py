from django.db import models
from account.models import User
from category.models import Category

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to = 'vendorprofile', blank=True)
    place = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    is_subscribed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)


class VendorSubscription(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=10)
    subscription_amount = models.CharField(max_length=10, blank=True)
    subscription_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(auto_now=True)


    def __str__(self):
        return str(self.user)


#sub type