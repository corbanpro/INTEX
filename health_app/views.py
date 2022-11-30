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

    return dashboardPageView(request, new_user.id)


def dashboardLoginPageView(request) :
    useremail = request.GET.get('email')
    userpassword = request.GET.get('password')

    try :
        user = User.objects.get(email = useremail, password = userpassword)

    except :

        return render(request, 'health_app/login.html')

    # context = {
    #     'user' : user
    # }

    return dashboardPageView(request, user.id)


def dashboardPageView(request, user_id=1, recipe_name=None, ingredient_name=None, ingredient_id=None) :

    if recipe_name != None :
        recipe_dict = searchRecipes(recipe_name)
    else :
        recipe_dict = dict()

    if ingredient_name != None :
        ingredient_dict = searchIngredients(ingredient_name)
    else :
        ingredient_dict = dict()

    if ingredient_id != None :
        measure_list = getIngredientInformation1(ingredient_id)
    else :
        measure_list = list()
    
    user = User.objects.get(id = user_id)

    today = datetime.now().date()
    meal_dict = Meal.objects.filter(date = today, user = user_id)

    recipe_list = list()
    for meal in meal_dict :
        recipe_list.append(Recipe.objects.get(id = meal.recipe.id))

    totalCarb = 0
    totalPro = 0
    totalFat = 0
    totalWat = 0
    totalSod = 0
    totalPho = 0
    totalPot = 0

    for recipe in recipe_list :
        totalCarb += recipe.carbs
        totalPro += recipe.protein
        totalFat += recipe.fat
        totalWat += recipe.water
        totalSod += recipe.sodium
        totalPho += recipe.phosphorus
        totalPot += recipe.potassium


    context = {
        'user' : user,
        'fCarb': totalCarb,
        'fPro' : totalPro,
        'fFat' : totalFat,
        'fWat' : totalWat,
        'fSod' : totalSod,
        'fPho' : totalPho,
        'fPot' : totalPot,
        'recipe_dict' : recipe_dict,
        'ingredient_dict' : ingredient_dict,
        'ingredient_id' : ingredient_id,
        'measure_list' : measure_list,


    }

    return render(request, 'health_app/dash.html', context)


def dashboardRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)
    recipe_name = request.GET['recipe_name']
    # context = {
    #     'recipe_dict' : searchRecipes(recipe_name),
    #     'user' : user
    # }

    return dashboardPageView(request, user_id, recipe_name=recipe_name)


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
    new_recipe.phosphorus = recipe_dict['phosphorus']
    new_recipe.sodium = recipe_dict['sodium']
    new_recipe.calories = recipe_dict['calories'] 
    new_recipe.save()

    new_meal = Meal()
    new_meal.date = datetime.now().date()
    new_meal.recipe = new_recipe
    new_meal.user = user
    new_meal.save()


    # context = {
    #     'user' : user

    # }

    return dashboardPageView(request, user_id)


def dashboardIngredientPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    ingredient_name = request.GET['ingredient_name']

    # context = {
    #     'ingredient_dict' : searchIngredients(ingredient_name),
    #     'user' : user

    # }

    return dashboardPageView(request, user_id, ingredient_name=ingredient_name)


def dashboardIngredientUnitPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    ingredient_id = request.GET['selected_ingredient']

    # context = {
    #     'measure_list' : getIngredientInformation1(ingredient_id),
    #     'ingredient_id' : ingredient_id,        
    #     'user' : user,

    # }

    return dashboardPageView(request, user_id, ingredient_id=ingredient_id)


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
    new_ingredient.phosphorus = ingredient_dict['phosphorus']
    new_ingredient.sodium = ingredient_dict['sodium']
    new_ingredient.calories = ingredient_dict['calories'] 
    new_ingredient.save()

    new_meal = Meal()
    new_meal.date = datetime.now().date()
    new_meal.recipe = new_ingredient
    new_meal.user = user
    new_meal.save()


    # context = {
    #     'user' : user
    # }

    return dashboardPageView(request, user_id)


def addWaterPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    amount = request.GET['water_added']

    water = Recipe()
    water.name = 'water'
    water.water = amount
    water.save()

    new_meal = Meal()
    new_meal.date = datetime.now().date()
    new_meal.recipe = water
    new_meal.user = user
    new_meal.save()

    # context = {
    #     'user' : user
    # }

    return dashboardPageView(request, user_id)


def historyPageView(request, user_id, recipe_name=None, ingredient_name=None, ingredient_id=None) :
    if recipe_name != None :
        recipe_dict = searchRecipes(recipe_name)
    else :
        recipe_dict = dict()

    if ingredient_name != None :
        ingredient_dict = searchIngredients(ingredient_name)
    else :
        ingredient_dict = dict()

    if ingredient_id != None :
        measure_list = getIngredientInformation1(ingredient_id)
    else :
        measure_list = list()

    user = User.objects.get(id = user_id)

    ### does this return an object or a return string
    meal_dict = Meal.objects.filter(user = user_id)
    recipe_list = list()
    for meal in meal_dict :
        recipe_list.append(Recipe.objects.get(id = meal.recipe.id))

    totalCarb = 0
    totalPro = 0
    totalFat = 0
    totalWat = 0
    totalSod = 0
    totalPho = 0
    totalPot = 0

    for recipe in recipe_list :
        totalCarb += recipe.carbs
        totalPro += recipe.protein
        totalFat += recipe.fat
        totalWat += recipe.water
        totalSod += recipe.sodium
        totalPho += recipe.phosphorus
        totalPot += recipe.potassium

    #here we need to put if statements for the alerts
    #so for example if totalCarb > dailyValueDeterminante.protein for the user
    #then "color" : rgb122 (whatever red is) and "message" = "You have exceeded the daily value for protein."
    #We will NOT do this for carbs, calories, or fats as they do not have UL
    #We will consider the values in the table provided by client as Upper Limits

    context = {
        'user' : user,
        'fCarb': totalCarb,
        'fPro' : totalPro,
        'fFat' : totalFat,
        'fWat' : totalWat,
        'fSod' : totalSod,
        'fPho' : totalPho,
        'fPot' : totalPot,
        'recipe_dict' : recipe_dict,
        'ingredient_dict' : ingredient_dict,
        'ingredient_id' : ingredient_id,
        'measure_list' : measure_list,
    }
    return dashboardPageView(request, user_id)

    




