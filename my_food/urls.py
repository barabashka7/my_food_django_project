from django.urls import path
from . import views

urlpatterns = [
    path('food', views.edit_food,name='edit_food'),
    path('recipe', views.show_recipes, name='show_recipes'),
    path('add_recipe', views.add_recipe, name='add_recipe')
]
