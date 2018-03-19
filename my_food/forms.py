from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, UserIngredient,Comment


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RecipeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows':"3"}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"3"}))
    text_recipe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"16"}))
    img_main = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    img1 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    img2 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    img3 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    class Meta:
        model = Recipe
        fields = ('title','description','ingredients','text_recipe','img_main','img1','img2','img3')

class UserIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ('food',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)