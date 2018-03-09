from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, UserIngredient


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title','description','ingredients','text_recipe','img_main','img1','img2','img3')



class UserIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ('food',)