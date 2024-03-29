from django.db import models


# Create your models here.
class Hero(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name  + '' + self.last_name
