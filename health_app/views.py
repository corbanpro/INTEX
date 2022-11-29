from django.shortcuts import render
from .functions import searchRecipes, getRecipeInformation, searchIngredients, getIngredientInformation1, getIngredientInformation2
from .models import user, recipe, meal
from datetime import datetime
from django.http import HttpResponse


def indexPageView(request) :
    context = {
        'recipedict' : searchRecipes('chicken quesadilla')
    }
    return render(request, 'health_app/index.html', context)

def dashboardPageView(request) :
    context = {
        'recipe_dict' : {},
        'userID' : 1
    }

    return render(request, 'health_app/dash.html', context)

def dashboardRecipePageView(request) :
    recipe_name = request.GET['recipe_name']
    context = {
        'recipe_dict' : searchRecipes(recipe_name),
        'userID' : 1
    }

    return render(request, 'health_app/dash.html', context)

def addRecipePageView(request) :
    recipe_id = request.POST['selected_recipe']
    recipe_dict = getRecipeInformation(recipe_id)

    new_recipe = recipe()

    new_recipe.name = recipe_dict['title']
    new_recipe.fat = recipe_dict['fat']
    new_recipe.protein = recipe_dict['protein']
    new_recipe.carbs = recipe_dict['carbs']
    new_recipe.potassium = recipe_dict['potassium']
    new_recipe.phosphorous = recipe_dict['phosphorus']
    new_recipe.sodium = recipe_dict['sodium']
    new_recipe.calories = recipe_dict['calories'] 
    new_recipe.save()

    new_meal = meal()
    new_meal.datetime = datetime.now()
    new_meal.recipe = new_recipe
    # new_meal.user = user
    # new_meal.save()


    context = {

    }

    return render(request, 'health_app/dash.html', context)

def dashboardIngredientPageView(request) :
    ingredient_name = request.GET['ingredient_name']

    context = {
        'ingredient_dict' : searchIngredients(ingredient_name),
    }

    return render(request, 'health_app/dash.html', context)

def dashboardIngredientUnitPageView(request) :
    ingredient_id = request.GET['selected_ingredient']

    context = {
        'measure_list' : getIngredientInformation1(ingredient_id),
        'ingredient_id' : ingredient_id
    }

    return render(request, 'health_app/dash.html', context)

def addIngredientPageView(request, ingredient_id) :
    amount = request.POST.get('selected_amount')
    unit = request.POST.get('selected_unit')
    ingredient_dict = getIngredientInformation2(ingredient_id, amount, unit)

    new_ingredient = recipe()

    new_ingredient.name = ingredient_dict['name']
    new_ingredient.fat = ingredient_dict['fat']
    new_ingredient.protein = ingredient_dict['protein']
    new_ingredient.carbs = ingredient_dict['carbs']
    new_ingredient.potassium = ingredient_dict['potassium']
    new_ingredient.phosphorous = ingredient_dict['phosphorus']
    new_ingredient.sodium = ingredient_dict['sodium']
    new_ingredient.calories = ingredient_dict['calories'] 
    new_ingredient.save()


    context = {

    }

    return render(request, 'health_app/dash.html', context)

def historyPageView(request) :
    return render(request, 'health_app/history.html')

def registerPageView(request) :
    return render(request, 'health_app/register.html')

def loginPageView(request) :
    return render(request, 'health_app/login.html')


