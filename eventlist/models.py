from statistics import mode
from django.db import models
from account.models import User
# Create your models here.


class EventList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, blank=True)
    event_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
