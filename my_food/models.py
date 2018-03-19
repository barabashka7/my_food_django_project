from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class CustomUser:
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    registration_date = models.DateTimeField(default = timezone.now)

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=400)
    text_recipe = models.TextField()
    ingredients = models.TextField(default="")
    img_main = models.ImageField(upload_to='photo/' ,height_field=None, width_field=None)
    img1 = models.ImageField(upload_to='photo/' ,height_field=None, width_field=None)
    img2 = models.ImageField(upload_to='photo/' ,height_field=None, width_field=None)
    img3 = models.ImageField(upload_to='photo/' ,height_field=None, width_field=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class UserIngredient(models.Model):
    food = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(max_length=250, blank=False)