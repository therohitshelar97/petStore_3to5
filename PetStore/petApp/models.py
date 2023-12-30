from django.db import models


# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    breed = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    desc = models.CharField(max_length=500,default=True,null=True)
    date = models.DateField(auto_now=True,null=True)
    time = models.TimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to='media',null=True)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

