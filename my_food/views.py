from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignUpForm, RecipeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Recipe
from django.http import HttpResponseNotFound


@login_required
def edit_food(request,user_id):
    return render(request, 'my_food/food.html', {})

@login_required
def show_recipes(request,user_id):
    pass

@login_required
def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except(Recipe.DoesNotExist):
        return HttpResponseNotFound
    return render(request,'my_food/recipe.html',{'recipe':recipe})

@login_required
def add_recipe(request, user_id):
    #user = User.objects.filter()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if(form.is_valid()):
            recipe = form.save()
            #recipe.author = user
            recipe.save()
            return redirect('recipe')
    else:
        form = RecipeForm()
    return(request,'my_food/add_recipe.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('edit_food')
    else:
        form = SignUpForm()
    return render(request, 'my_food/signup.html', {'form': form})

