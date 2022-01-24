from django.db import models

# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.category_name)