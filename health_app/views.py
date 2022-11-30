from django.shortcuts import render
from .functions import searchRecipes, getRecipeInformation, searchIngredients, getIngredientInformation1, getIngredientInformation2
from .models import User, Recipe, Meal, Comorbidity
from datetime import datetime
from django.http import HttpResponse


def indexPageView(request) :
    context = {
    }
    return render(request, 'health_app/index.html', context)


def loginPageView(request) :
    return render(request, 'health_app/login.html')


def registerPageView(request) :
    return render(request, 'health_app/register.html')

## Create a new User
def dashboardUserPageView(request):

    new_user = User()
    new_user.firstName = request.POST.get('first_name')
    new_user.lastName = request.POST.get('last_name')
    new_user.email = request.POST.get('inputEmail')
    new_user.password = request.POST.get('inputPassword')
    new_user.sex = request.POST.get('listSex')
    feet_ht = int(request.POST.get('txtFtHeight'))
    in_ht = int(request.POST.get('txtInHeight'))
    tot_ht = (feet_ht * 12) + in_ht
    new_user.height = tot_ht
    new_user.weight = request.POST.get('txtWeight')
    new_user.birthDate = request.POST.get('birth_date')
    if request.POST.get('cbHBP') == 'HBP' : 
        HBP = True
    else : 
        HBP = False
    if request.POST.get('cbDiabetes') == 'Diabetes' : 
        DB = True
    else :
        DB = False
    KDS = request.POST.get('comorb_kds')
    new_user.comorbidity = Comorbidity.objects.get(highBloodPressure = HBP, diabetes = DB, kidneyDiseaseStage = KDS)
    new_user.save()


    context = {
        'user' : new_user
    }

    return render(request, 'health_app/dash.html', context)

    return HttpResponse('failure')


def dashboardLoginPageView(request) :
    useremail = request.GET.get('email')
    userpassword = request.GET.get('password')

    try :
        user = User.objects.get(email = useremail, password = userpassword)

    except :

        return render(request, 'health_app/login.html')

    context = {
        'user' : user
    }

    return render(request, 'health_app/dash.html', context)


def dashboardPageView(request) :
    recipeToFind = 'Peeta Bread'
    fCarb = Recipe.objects.filter(name = recipeToFind).values('carbs')[0]['carbs']
    fPro = Recipe.objects.filter(name = recipeToFind).values('protein')[0]['protein']
    fFat = Recipe.objects.filter(name = recipeToFind).values('fat')[0]['fat']
    fWat = Recipe.objects.filter(name = recipeToFind).values('water')[0]['water']
    fSod = Recipe.objects.filter(name = recipeToFind).values('sodium')[0]['sodium']
    fPho = Recipe.objects.filter(name = recipeToFind).values('phosphorous')[0]['phosphorous']
    fPot = Recipe.objects.filter(name = recipeToFind).values('potassium')[0]['potassium']


    context = {
        'user' : User,
        'userID' : 1,
        'fCarb': fCarb,
        'fPro' : fPro,
        'fFat' : fFat,
        'fWat' : fWat,
        'fSod' : fSod,
        'fPho' : fPho,
        'fPot' : fPot,
        'query' : str(fCarb)
    }

    return render(request, 'health_app/dash.html', context)


def dashboardRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)
    recipe_name = request.GET['recipe_name']
    context = {
        'recipe_dict' : searchRecipes(recipe_name),
        'user' : user
    }

    return render(request, 'health_app/dash.html', context)


def addRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)

    recipe_id = request.POST['selected_recipe']
    recipe_dict = getRecipeInformation(recipe_id)

    new_recipe = Recipe()

    new_recipe.name = recipe_dict['title']
    new_recipe.fat = recipe_dict['fat']
    new_recipe.protein = recipe_dict['protein']
    new_recipe.carbs = recipe_dict['carbs']
    new_recipe.potassium = recipe_dict['potassium']
    new_recipe.phosphorous = recipe_dict['phosphorus']
    new_recipe.sodium = recipe_dict['sodium']
    new_recipe.calories = recipe_dict['calories'] 
    new_recipe.save()

    new_meal = Meal()
    new_meal.datetime = datetime.now()
    new_meal.recipe = new_recipe
    # new_meal.user = user
    # new_meal.save()


    context = {
        'user' : user

    }

    return render(request, 'health_app/dash.html', context)


def dashboardIngredientPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    ingredient_name = request.GET['ingredient_name']

    context = {
        'ingredient_dict' : searchIngredients(ingredient_name),
        'user' : user

    }

    return render(request, 'health_app/dash.html', context)


def dashboardIngredientUnitPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    ingredient_id = request.GET['selected_ingredient']

    context = {
        'measure_list' : getIngredientInformation1(ingredient_id),
        'ingredient_id' : ingredient_id,
        'user' : user,

    }

    return render(request, 'health_app/dash.html', context)


def addIngredientPageView(request, ingredient_id, user_id) :
    user = User.objects.get(id = user_id)

    amount = request.POST.get('selected_amount')
    unit = request.POST.get('selected_unit')
    ingredient_dict = getIngredientInformation2(ingredient_id, amount, unit)

    new_ingredient = Recipe()

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
        'user' : user
    }

    return render(request, 'health_app/dash.html', context)


def addWaterPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    amount = request.GET['water_added']

    water = Recipe()
    water.name = 'water'
    water.water = amount
    water.save()
    context = {
        'user' : user
    }

    return render(request, 'health_app/dash.html', context)


def historyPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    context = {
        'user' : user
    }
    return render(request, 'health_app/history.html', context)

    




