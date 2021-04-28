from django.db import models
from mycakes.models import Cakes


class Order(models.Model):
    # orderid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=250, blank=True, null=True )
    city = models.CharField(max_length=250, blank=True, null=True )
    mode = models.CharField(max_length=250, default='cash',blank=True, null=True)
    pending = models.BooleanField(default=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    cakes = models.ManyToManyField(Cakes, blank=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.email


class UserDetails(models.Model):
    email = models.CharField(max_length=250,blank=True)
    cart = models.ManyToManyField(Cakes, blank=True)
    def __str__(self):
        return self.email

