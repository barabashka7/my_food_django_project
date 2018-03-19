from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignUpForm, RecipeForm, UserIngredientForm, CommentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Recipe, UserIngredient, Comment, CustomUser
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone

def index(request):
    return render(request, 'my_food/index.html',{})

@login_required
def prof(request):
    user = request.user
    kol_of_ingredients = UserIngredient.objects.filter(user=user).count()
    recipes = Recipe.objects.filter(author=user)
    kol_of_recipes = recipes.count()
    kol_of_comments = Comment.objects.filter(author=user).count()
    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            password = form.cleaned_data["new_password1"]
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('prof')
    else:
        form = PasswordChangeForm(user)
    return render(request,'my_food/prof.html',{'form': form,
                                               'recipes': recipes,
                                               'kol_of_ingredients': kol_of_ingredients,
                                               'kol_of_recipes': kol_of_recipes,
                                               'kol_of_comments': kol_of_comments})

@login_required
def add_recipe(request):
    user = request.user
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        form.instance.author = user
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('recipe',recipe_id=recipe.pk)
    else:
        form = RecipeForm()
    return render(request,'my_food/add_recipe.html',{'form': form})

@login_required
def edit_food(request):
    user = request.user
    ingredients = UserIngredient.objects.filter(user=user)
    if request.method == "POST":
        form = UserIngredientForm(request.POST)
        form.instance.user = user
        if form.is_valid():
            ingredient = form.save()
            ingredient.save()
            return redirect('edit_food')
    else: form = UserIngredientForm()
    return render(request, 'my_food/food.html', {'ingredients': ingredients, 'form': form})

@login_required
def ingredient(request, ingredient_id):
    ingredient=UserIngredient.objects.get(id=ingredient_id)
    if request.user == ingredient.user:
        ingredient.delete()
        return redirect('edit_food')

@login_required
def recipes(request):
    user = request.user
    user_ingredients = UserIngredient.objects.filter(user=user)
    ingredients = []
    for user_ingredient in user_ingredients:
        ingredients.append(user_ingredient.food.lower())
    all_recipes=Recipe.objects.all()
    recipes = []
    for recipe in all_recipes:
        ingredients_of_recipe=recipe.ingredients.split(', ')
        flag=True
        for ingredient in ingredients_of_recipe:
            if(not ingredient.lower() in ingredients):
                flag=False
                break
        if(flag):
            recipes.append(recipe)
    return render(request, 'my_food/recipes.html',{'recipes': recipes})

@login_required
def edit_recipe(request, recipe_id):
    user=request.user
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author == user:
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            form.instance.author = user
            if form.is_valid():
                recipe = form.save()
                recipe.save()
                return redirect('recipe', recipe_id=recipe.pk)
        else:
            form = RecipeForm(instance=recipe)
    else:
        return HttpResponseNotFound
    return render(request, "my_food/edit_recipe.html", {'form': form})

@login_required
def recipe(request, recipe_id):
    user = request.user
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        comments = Comment.objects.filter(recipe__pk=recipe_id)
    except(Recipe.DoesNotExist):
        return HttpResponseNotFound
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe=recipe
            comment.author=request.user
            comment.save()
            return redirect('recipe', recipe_id=recipe.pk)
    else:
        form=CommentForm()
    return render(request,'my_food/recipe.html',{'recipe': recipe,
                                                 'comments': comments,
                                                 'user': user,
                                                 'form':  form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            custom_user=CustomUser()
            custom_user.user=user
            custom_user.registration_date=timezone.now()
            return redirect('prof')
    else:
        form = SignUpForm()
    return render(request, 'my_food/signup.html', {'form': form})

