from django.shortcuts import render
from .functions import searchRecipes, getRecipeInformation
from .models import user, recipe, meal
from datetime import datetime


def indexPageView(request) :
    context = {
        'recipedict' : searchRecipes('chicken quesadilla')
    }
    return render(request, 'health_app/index.html', context)

def dashboardPageView(request, user) :
    context = {
        'user' : user,
        'userID' : 1
    }

    return render(request, 'health_app/dash.html', context)

## Create a new User
def newUser(user_credentials):
    new_user = user()
    new_user.firstName = user_credentials['first_name']
    new_user.lastName = user_credentials['last_name']
    new_user.email = user_credentials['email']
    new_user.password = user_credentials['password']
    new_user.sex = user_credentials['sex']
    new_user.height = user_credentials['height']
    new_user.weight = user_credentials['weight']
    new_user.birthDate = user_credentials['birth_date']
    new_user.comorbidity = user_credentials['comorbidity']

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



def historyPageView(request) :
    return render(request, 'health_app/history.html')

def registerPageView(request) :
    return render(request, 'health_app/register.html')

def loginPageView(request) :
    return render(request, 'health_app/login.html')


