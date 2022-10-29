from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Transaction(models.Model):
    date = models.DateField(default=datetime.date.today)
    exp = models.CharField(max_length=1000) #explanation
    deb = models.IntegerField(default=0) #debtor
    cred = models.IntegerField(default=0) #creditor
    remain = models.IntegerField(default=0)

class Ustable(models.Model):
    title = models.CharField(max_length=50)
    tranactions = models.ManyToManyField(Transaction)
    class Meta:
        ordering = ['title']

