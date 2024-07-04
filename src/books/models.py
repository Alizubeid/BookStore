from django.db import models
from accounts.models import Auther

class Book(models.Model):
    title = models.CharField(max_length=100)
    auther = models.ForeignKey(Auther,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=400)