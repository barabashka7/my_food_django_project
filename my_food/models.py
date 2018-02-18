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
    place = models.OneToOneField(
        UserFood,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class UserFood(models.Model):
    my_food = ?

