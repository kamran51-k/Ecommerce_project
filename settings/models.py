from django.db import models
from django.db.models.fields import BooleanField, CharField

# Create your models here.
class NavbarModel(models.Model):
    title = CharField(max_length=100,null=True,blank=True)
    category = BooleanField()

class CategoryModel(models.Model):
    style = CharField(max_length=100,null=True,blank=True)