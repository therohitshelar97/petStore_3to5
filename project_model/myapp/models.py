from django.db import models

# Create your models here.
class Data(models.Model):
    pname = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    salary = models.FloatField(null=True)
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.pname
    