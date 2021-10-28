from django.db import models

# Create your models here.

class Library(models.Model):
    bname = models.CharField(max_length=100)
    bauthor = models.CharField(max_length=100)
    bquantity = models.IntegerField() 


# MEDIUM STACK OVERFLOW CRUD

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


################CRUD REST ###############

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)





################CRUD REST ###############
