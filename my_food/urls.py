from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit_food/', views.edit_food,name='edit_food'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('id<int:recipe_id>/', views.recipe, name='recipe'),
    path('id<int:recipe_id>/edit_recipe', views.edit_recipe, name='edit_recipe'),
    path('recipes/', views.recipes,name='recipes'),
    path('index/', views.index, name='index')
]
