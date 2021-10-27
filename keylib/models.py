from django.db import models

# Create your models here.

class Library(models.Model):
    bname = models.CharField(max_length=100)
    bauthor = models.CharField(max_length=100)
    bquantity = models.IntegerField() 