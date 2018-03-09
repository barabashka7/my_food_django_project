from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=400)
    text_recipe = models.TextField()
    ingredients = models.TextField(default="")
    img_main = models.ImageField(upload_to='photo/', blank=True,height_field=None, width_field=None)
    img1 = models.ImageField(upload_to='photo/', blank=True,height_field=None, width_field=None)
    img2 = models.ImageField(upload_to='photo/', blank=True,height_field=None, width_field=None)
    img3 = models.ImageField(upload_to='photo/', blank=True,height_field=None, width_field=None)

class UserIngredient(models.Model):
    food = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')
