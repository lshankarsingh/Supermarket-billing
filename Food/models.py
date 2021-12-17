from django.db import models

# Create your models here.
class Productslist(models.Model):
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    subcategory=models.CharField(max_length=20)
    amount=models.IntegerField()
