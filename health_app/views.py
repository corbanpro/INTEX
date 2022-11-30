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
    recipeToFind = 'Peeta Bread'
    fCarb = recipe.objects.filter(name = recipeToFind).values('carbs')[0]['carbs']
    fPro = recipe.objects.filter(name = recipeToFind).values('protein')[0]['protein']
    fFat = recipe.objects.filter(name = recipeToFind).values('fat')[0]['fat']
    fWat = recipe.objects.filter(name = recipeToFind).values('water')[0]['water']
    fSod = recipe.objects.filter(name = recipeToFind).values('sodium')[0]['sodium']
    fPho = recipe.objects.filter(name = recipeToFind).values('phosphorous')[0]['phosphorous']
    fPot = recipe.objects.filter(name = recipeToFind).values('potassium')[0]['potassium']


    context = {
        'user' : user,
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

## Create a new User
def dashboardUserPageView(request):

    if request.method == 'Post':
        new_user = user()
        new_user.firstName = request.GET['first_name']
        new_user.lastName = request.GET['last_name']
        new_user.email = request.GET['inputEmail']
        new_user.password = request.GET['inputPassword']
        new_user.sex = request.GET['listSex']
        feet_ht = int(request.GET['txtFtHeight'])
        in_ht = int(request.GET['txtInHeight'])
        tot_ht = (feet_ht * 12) + in_ht
        new_user.height = tot_ht
        new_user.weight = request.GET['txtWeight']
        new_user.birthDate = request.GET['birth_date']
        comorb_list = []
        if request.GET['cbHBP'] == 'HBP' and request.GET['cbDiabetes'] == 'Diabetes':
            comorb = comorbidity()
            comorb.KidneyDiseaseStage = request.GET['comorb_kds']
            comorb.highBloodPressure = True
            comorb.diabetes = True
            ## append comorbidity object
            comorb.append('High Blood Pressure')
        elif request.GET['cbDiabetes'] == 'Diabetes':
            comorb = comorbidity()
            comorb.KidneyDiseaseStage = request.GET['comorb_kds']
            comorb.highBloodPressure = False
            comorb.diabetes = True
        elif request.GET['cbHBP'] == 'HBP':
            comorb = comorbidity()
            comorb.KidneyDiseaseStage = request.GET['comorb_kds']
            comorb.highBloodPressure = True
            comorb.diabetes = False
        
        new_user.comorbidity = comorb

        new_user.save()

        dashboardPageView(request, 'health_app/dash.html')


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

def addWaterPageView(request) :
    amount = request.GET['water_added']

    water = recipe()
    water.name = 'water'
    water.water = amount
    water.save()

    return render(request, 'health_app/dash.html')


def historyPageView(request) :
    return render(request, 'health_app/history.html')

def registerPageView(request) :
    return render(request, 'health_app/register.html')

def loginPageView(request) :
    return render(request, 'health_app/login.html')

def dashboardLoginPageView(request) :
    useremail = request.GET.get('email')
    userpassword = request.GET.get('password')

    try :
        USER = user.objects.get(email = useremail, password = userpassword)
    except :
        
        return render(request, 'health_app/login.html')

    context = {
        'user' : USER
    }

    return render(request, 'health_app/dash.html', context)


    




