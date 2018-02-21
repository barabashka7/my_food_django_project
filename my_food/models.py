from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=300)
    text_recipe = models.TextField()
    img_main = models.ImageField()
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    ingredients = models.TextField()

class CustomUser(User):
    objects = UserManager()
    ingredients = []

class Ingredient(models.Model):
    food = models.CharField(max_length=35)
    kol_of_food = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
