from django.db import models
from accounts.models import User

# Create your models here.


class Professionals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, null=True)
    full_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to = 'vendorprofile', blank=True)
    place = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return str(self.user)

    
