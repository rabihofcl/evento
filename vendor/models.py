from django.db import models
from account.models import User
from category.models import Category

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to = 'vendorprofile', blank=True)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    subscription_type = models.CharField(max_length=10)
    subscription_amount = models.CharField(max_length=10)
    subscription_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user)
