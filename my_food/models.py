from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=300)
    text_recipe = models.TextField()
    img_main = models.ImageField()
    img1 = models.ImageField(upload_to='photo/', blank=True)
    img2 = models.ImageField(upload_to='photo/', blank=True)
    img3 = models.ImageField(upload_to='photo/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

"""class UserIngredient(models.Model):
    food = models.CharField(max_length=35)
    kol_of_food = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')

class RecipeIngredient(models.Model):
    food = models.CharField(max_length=35)
    kol_of_food = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')"""
