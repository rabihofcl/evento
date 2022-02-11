from email.policy import default
from pyexpat import model
from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

# def upload_to(instance, filename):
#     return 'vendor-profile/{filename}'.format(filename=filename)


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True)
    profile_picture = models.FileField(upload_to='media/vendor-profile/')
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    image1 = models.FileField(upload_to='media/showcase/', blank=True)
    image2 = models.FileField(upload_to='media/showcase/', blank=True)
    image3 = models.FileField(upload_to='media/showcase/', blank=True)
    image4 = models.FileField(upload_to='media/showcase/', blank=True)
    image5 = models.FileField(upload_to='media/showcase/', blank=True)
    image6 = models.FileField(upload_to='media/showcase/', blank=True)
    subscription_type = models.CharField(max_length=10)
    subscription_amount = models.CharField(max_length=10)
    subscription_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class VendorSlots(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    busy_slots = models.JSONField(blank=True)
    booked_slots = models.JSONField(blank=True)

    def __str__(self):
        return str(self.user)    