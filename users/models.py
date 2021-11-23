from typing import Sized
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    job  = models.CharField(max_length=100)

    class Meta: 
        db_table = "persons"