from django.db import models
import datetime
# Create your models here.


class Cakes(models.Model):
    cakeid = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(default=datetime.datetime.now())
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=550)
    type = models.CharField(max_length=550)
    ingredients = models.CharField(max_length=250)
    eggless = models.BooleanField(default=True)
    image = models.ImageField(upload_to='cakeimages/', blank=True, null=True)
    flavour = models.CharField(max_length=550)
    price = models.FloatField()
    weight = models.IntegerField()
    rating = models.FloatField(default=4.5)
    review = models.IntegerField(default=4)
    likes = models.IntegerField(default=4)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
