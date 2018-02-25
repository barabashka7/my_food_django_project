from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('id<int:user_id>/edit_food/', views.edit_food,name='edit_food'),
    path('id<int:user_id>/add_recipe/', views.add_recipe, name='add_recipe'),
    path('id<int:recipe_id>/', views.recipe, name='recipe'),
    path('id<int:user_id>/recipes/', views.show_recipes,name='show_recipes')
]
