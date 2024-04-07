from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100,default="Empty")
    price = models.IntegerField(default=0.00)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name