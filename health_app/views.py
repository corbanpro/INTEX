from django.shortcuts import render
from .functions import searchRecipes, getRecipeInformation, searchIngredients, getIngredientInformation1, getIngredientInformation2, searchRecipeByNutrient
from .models import User, Recipe, Meal, DvDeterminate, DailyValue
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

#dashboardUserPageView is the path to dashboard THROUGH register that creates a user and opens dash
def dashboardUserPageView(request):

    #this generates a new user obeject using the information received through registering
    new_user = User()
    new_user.firstName = request.POST.get('first_name')
    new_user.lastName = request.POST.get('last_name')
    new_user.email = request.POST.get('inputEmail')
    new_user.password = request.POST.get('inputPassword')
    feet_ht = int(request.POST.get('txtFtHeight'))
    in_ht = int(request.POST.get('txtInHeight'))
    tot_ht = (feet_ht * 12) + in_ht
    new_user.height = tot_ht
    new_user.weight = request.POST.get('txtWeight')
    new_user.birthDate = request.POST.get('birth_date')

    #this capaitalizes the sex correctly
    user_sex = request.POST.get('listSex')

    #this enters in if they have high blood pressure
    if request.POST.get('cbHBP') == 'HBP' : 
        HBP = True
    else : 
        HBP = False

    #this enters in if they have diabetes
    if request.POST.get('cbDiabetes') == 'Diabetes' : 
        DB = False
    else :
        DB = False

    #this enters in the stage of kidney disease they have 
    KDS = request.POST.get('comorb_kds')


    try :
        new_user.dv_determinate = DvDeterminate.objects.get(sex = user_sex, highBloodPressure = HBP, diabetes = DB, kidneyDiseaseStage = KDS)

    except :
        new_dv_determinate = DvDeterminate()
        new_dv_determinate.sex = user_sex

        if HBP :
            new_dv_determinate.highBloodPressure = True
        else :
            new_dv_determinate.highBloodPressure = False

        if DB :
            new_dv_determinate.diabetes = True
        else :
            new_dv_determinate.diabetes = False 
            
        new_dv_determinate.kidneyDiseaseStage = KDS
        if user_sex == 'Male' :
            new_dv_determinate.daily_value = DailyValue.objects.get(id = 1)
        else :
            new_dv_determinate.daily_value = DailyValue.objects.get(id = 2)
        new_dv_determinate.save()

        new_user.dv_determinate = new_dv_determinate
    
    new_user.save()


    context = {
        'user' : new_user
    }

    return dashboardPageView(request, new_user.id)

#this is the path to dash if a user logged in (as opposed to registering)
def dashboardLoginPageView(request) :
    useremail = request.POST.get('email')
    userpassword = request.POST.get('password')

    #checks if the useremail and password match
    try :
        user = User.objects.get(email = useremail, password = userpassword)

    except :

        return render(request, 'health_app/login.html')

    return dashboardPageView(request, user.id)

#this dash page view renders more specifics about the graphs on the users age 
def dashboardPageView(request, user_id=1, recipe_name=None, ingredient_name=None, ingredient_id=None, selection = 'protein') :

    #search recipes
    if recipe_name != None :
        recipe_dict = searchRecipes(recipe_name)
    else :
        recipe_dict = dict()

    #search ingredients
    if ingredient_name != None :
        ingredient_dict = searchIngredients(ingredient_name)
    else :
        ingredient_dict = dict()

    #enter measurement for ingredients
    if ingredient_id != None :
        measure_list = getIngredientInformation1(ingredient_id)
    else :
        measure_list = list()
    
    #find user and day and add the ingredient or recipe to their recorded meals for the day 
    user = User.objects.get(id = user_id)

    today = datetime.now().date()
    meal_dict = Meal.objects.filter(date = today, user = user_id)

    recipe_list = list()
    for meal in meal_dict :
        recipe_list.append(Recipe.objects.get(id = meal.recipe.id))

    #########################
    ### this is pickNut function to select which nutrient to view and display it on the doughnut chart
    #########################
    selection = request.POST.get('nutList')

    #create empty lists for each possible ingredient
    foodList = []
    proteinList = []
    carbList = []
    fatList = []
    sodList = []
    phoList = []
    potList = []
    calList = []

    #iterate through the recipe list and append each of the nutrient levels to the corresponding nutrient list
    for recipe in recipe_list:
        foodList.append(recipe.name)
        proteinList.append(recipe.protein)
        calList.append(recipe.calories)
        carbList.append(recipe.carbs)
        fatList.append(recipe.fat)
        sodList.append(recipe.sodium)
        phoList.append(recipe.phosphorus)
        potList.append(recipe.potassium)

    #based on what nutrient the user selected to view, show that data and selection string
    if selection == 'Potassium':
        nutrientList = potList
        nutSelectOpt = 'Potassium (mg)'
    elif selection == 'Calories':
        nutrientList = calList
        nutSelectOpt = 'Calories '
    elif selection == 'Carbs':
        nutrientList = carbList
        nutSelectOpt = 'Carbs (g)'
    elif selection == 'Fat':
        nutrientList = fatList
        nutSelectOpt = 'Fat (g)'
    elif selection == 'Sodium':
        nutrientList = sodList
        nutSelectOpt = 'Sodium (mg)'
    elif selection == 'Phosphorus':
        nutrientList = phoList
        nutSelectOpt = 'Phosphorous (mg)'
    else :
        nutrientList = proteinList
        nutSelectOpt = 'Protein (g)'
    

    #this determines the daily value of the user and assigns it to a variable
    daily_val = DailyValue.objects.get(id = user.dv_determinate.daily_value.id)

    #initialize total nutrient levels of the day at zero
    tCarbs = 0
    tPro = 0
    tFat = 0
    tWat = 0
    tSod = 0
    tPho = 0
    tPot = 0

    #now add the nutrients to that variable to create a sum of the nutrients a user has had in a day
    for recipe in recipe_list :
        tCarbs += recipe.carbs
        tPro += recipe.protein
        tFat += recipe.fat
        tWat += recipe.water
        tSod += recipe.sodium
        tPho += recipe.phosphorus
        tPot += recipe.potassium

    #this code would be used by future developers to determine nutrient needs based on BMI
    #for the scope of our week long project, we did not incooperate this ourselves, but wanted to show a possible idea
    # avgBmi = 21.7
    # bmi = (user.weight / user.height**2) * 703
    # bmiCoef = bmi / avgBmi # maybe add some other random coefficient here to make the effect stronger or weaker. idk

    # this creates variables to hold the recommended amount of each nutrient for a person
    #you COULD do math according to BMI here but we will not
    dvCarbs = daily_val.carbs    # * bmiCoef
    dvPro = daily_val.protein * user.weight / 2.2    # * bmiCoef
    dvFat = daily_val.fat        # * bmiCoef
    dvWat = daily_val.water      # * bmiCoef
    dvSod = daily_val.sodium     # * bmiCoef
    dvPho = daily_val.phosphorus # * bmiCoef
    dvPot = daily_val.potassium  # * bmiCoef

    #now we deivde the sum amount a person has consumed of a nutrient by the recommended amount to find a percentage consumed
    pdvCarbs = (tCarbs / dvCarbs) * 100
    pdvPro = (tPro / dvPro) * 100
    pdvFat = (tFat / dvFat) * 100
    pdvWat = (tWat / dvWat) * 100
    pdvSod = (tSod / dvSod) * 100
    pdvPho = (tPho / dvPho) * 100
    pdvPot = (tPot / dvPot) * 100
    
    #we add these precentages to a list, this will help us display data later
    pdvList = [pdvCarbs, pdvPro, pdvFat, pdvWat, pdvSod, pdvPho, pdvPot]

    #create empty list regarding colors -the list will correlate to pdvList
    colorVar = []
    
    #iterate through pdvList, determine how high the percentage is using if statements to determine the 
    #color of the bar in the bar chart
    for pdv in pdvList :

        #red if over 100
        if pdv> 101 :
            colorVar.append('rgba(217, 30, 24, 0.8)')
        #green if between 85 and 100
        elif pdv >= 85 :
            colorVar.append('rgba(46, 204, 113, 0.8)')
        #yellow if below 85
        else :
            colorVar.append('rgba(228, 208, 10, 0.8)')

    #initialize sMessage as empty string
    sMessage = ""

    #only drop into this for loop if something has been exeeded
    if pdvCarbs >= 100 or pdvPro >= 100 or pdvFat >= 100 or pdvWat >= 100 or pdvSod >= 100 or pdvPho >= 100 or pdvPot >= 100 :
        exceededList = []
        sMessage = "You have exceeded the daily recommended intake for the following: "

        #these if statements determine which nutrients exceed 100% and append their names to the exceededList
        if pdvCarbs >= 100 :
            exceededList.append("carbs")
        else:
            pass

        if pdvPro >= 100 :
            exceededList.append("protein")
        else:
            pass

        if pdvFat >= 100 :
            exceededList.append("fat")
        else:
            pass

        if pdvWat >= 100 :
            exceededList.append("water")
        else:
            pass

        if pdvSod >= 100 :
            exceededList.append("sodium")
        else:
            pass

        if pdvPho >= 100 :
            exceededList.append("phosphorous")
        else:
            pass

        if pdvPot >= 100 :
            exceededList.append("potassium")
        else:
            pass

        #now we cylce through the exceeded list to add the names of the exceeded nutrients to the alert
        for exceeded in exceededList:
            length = len(exceededList)
            if exceededList.index(exceeded) == length - 1:
                sMessage += exceeded
                sMessage += '.'
            else:
                sMessage += exceeded
                sMessage += ', '

    #if there are no exceeded nutrients pass this whole step
    else:
        pass

    #this determines how much more g/mg of a nutrients are allowed for a user
    #these variables will be used to determine what recipes are safe to recommend to a person
    maxProtein = (dvPro - tPro) * 100
    maxSodium = (dvSod - tSod) * 100
    maxPhosphorus = (dvPho - tPho) * 100
    maxPotassium = (dvPot - tPot) * 100

    #if the negatives are erroring, try this instead
    #this will make anything that is a negtaive value equal to 0 instead
    try :

        maxProtein = (dvPro - tPro) * 100
        maxSodium = (dvSod - tSod) * 100
        maxPhosphorus = (dvPho - tPho) * 100
        maxPotassium = (dvPot - tPot) * 100

        if maxProtein < 0 :
            maxProtein = 0
        if maxSodium < 0 :
            maxSodium = 0
        if maxPhosphorus < 0 :
            maxPhosphorus = 0
        if maxPotassium < 0 :
            maxPotassium = 0

        suggested_recipeid_dict = searchRecipeByNutrient(maxProtein, maxPotassium, maxPhosphorus, maxSodium)

        suggested_recipeid_list = list()

        for recipe in suggested_recipeid_dict :
            suggested_recipeid_list.append(suggested_recipeid_dict[recipe])

        suggested_recipe_list = list()

        for id in suggested_recipeid_list :
            suggested_recipe_list.append(getRecipeInformation(id))

    except :
        suggested_recipe_list = list()

    #through one of the above methods, a list of recipes will be created 
    #this list will be displayed as recommended recipes on the dash page


    context = {
        'user' : user,
        'fCarb': pdvCarbs,
        'fPro' : pdvPro,
        'fFat' : pdvFat,
        'fWat' : pdvWat,
        'fSod' : pdvSod,
        'fPho' : pdvPho,
        'fPot' : pdvPot,
        'suggested_recipe_list' : suggested_recipe_list,
        'ingredient_name' : ingredient_name,
        'recipe_dict' : recipe_dict,
        'ingredient_dict' : ingredient_dict,
        'ingredient_id' : ingredient_id,
        'measure_list' : measure_list,
        'foodList' : foodList,
        'nutrientList' : nutrientList,
        'nutrientSelect': nutSelectOpt,
        'colLst' : colorVar,
        'sAlert' : sMessage,

    }

    return render(request, 'health_app/dash.html', context)

#this allows a user to view recipes (search)
def dashboardRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)
    recipe_name = request.GET['recipe_name']

    return dashboardPageView(request, user_id, recipe_name=recipe_name)

#this allows a user to add recipes to their record
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


    return dashboardPageView(request, user_id)

#allows user to search through foods (like bananas)
def dashboardIngredientPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    ingredient_name = request.GET['ingredient_name']

    return dashboardPageView(request, user_id, ingredient_name=ingredient_name)

#allows user to see and select the unit and amount of food they consumed
def dashboardIngredientUnitPageView(request, user_id, ingredient_name) :
    user = User.objects.get(id = user_id)

    ingredient_id = request.GET['selected_ingredient']

    return dashboardPageView(request, user_id, ingredient_id=ingredient_id, ingredient_name=ingredient_name)

#allows user to add food (like banana) to their record
def addIngredientPageView(request, ingredient_id, user_id, ingredient_name) :
    user = User.objects.get(id = user_id)

    amount = request.POST.get('selected_amount')
    unit = request.POST.get('selected_unit')
    ingredient_dict = getIngredientInformation2(ingredient_id, amount, unit)

    new_ingredient = Recipe()

    new_ingredient.name = ingredient_name
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


    return dashboardPageView(request, user_id)

# this allows a user to add water to their record
def addWaterPageView(request, user_id) :
    user = User.objects.get(id = user_id)

    amount = request.GET['water_added']

    water = Recipe()
    water.name = 'Water'
    water.water = amount
    water.save()

    new_meal = Meal()
    new_meal.date = datetime.now().date()
    new_meal.recipe = water
    new_meal.user = user
    new_meal.save()


    return dashboardPageView(request, user_id)

# this is the page view to see history (journal and nutrient intake history chart)
def historyPageView(request, user_id, recipe_name=None, ingredient_name=None, ingredient_id=None, selection = 'protein') :
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
    

    #get list of dates of the week, starting today going backward
    pastWeekDates = []
    from datetime import datetime, timedelta
    today = datetime.now().date()
    count = 0 
    while count < 8:
        dateToAdd = today - timedelta(days=count)
        dateToAdd = str(dateToAdd)
        count += 1
        pastWeekDates.append(dateToAdd)

    pastWeekDates.reverse()
    
    #according to dailyvalue table, determine the daily value of each nutrient
    daily_val = DailyValue.objects.get(id = user.dv_determinate.daily_value.id)
    dvCarbs = daily_val.carbs    # * bmiCoef
    dvPro = daily_val.protein * user.weight / 2.2   # * bmiCoef
    dvFat = daily_val.fat        # * bmiCoef
    dvWat = daily_val.water      # * bmiCoef
    dvSod = daily_val.sodium     # * bmiCoef
    dvPho = daily_val.phosphorus # * bmiCoef
    dvPot = daily_val.potassium  # * bmiCoef
    dvCal = daily_val.calories # *bmiCoef

    #initialize lists of recommended amounts of nutrients
    proRecList = []
    carbsRecList = []
    fatRecList = []
    watRecList = []
    sodRecList = []
    phoRecList = []
    potRecList = []
    calRecList = []

    #loop through these 7 times (to match one week) to add the recommended daily value of 
    #the nutrients (this will create a base line on chart to compare consumed nutrients to)
    count = 0 
    while count < 8:
        proRecList.append(dvPro)
        carbsRecList.append(dvCarbs)
        fatRecList.append(dvFat)
        watRecList.append(dvWat)
        sodRecList.append(dvSod)
        phoRecList.append(dvPho)
        potRecList.append(dvPot)
        calRecList.append(dvCal)
        count += 1

    #initialize empty lists that will contain the sum of what people actually ate in each day
    proActList = []   #sum of protein that person ate in one day
    carbsActList = []
    fatActList = []
    watActList = []
    sodActList = []
    phoActList = []
    potActList = []
    calActList = []

    #this is copy and pasted from the dashboard view function
    #this will create sums of each nutrient eaten each day
    for list_date in pastWeekDates:
        viz_meal_dict = Meal.objects.filter(date = list_date, user = user_id)

        recipe_list = list()
        for meal in viz_meal_dict :
            recipe_list.append(Recipe.objects.get(id = meal.recipe.id))

        totalCarb = 0
        totalPro = 0
        totalFat = 0
        totalWat = 0
        totalSod = 0
        totalPho = 0
        totalPot = 0
        totalCal = 0

        for recipe in recipe_list :
            totalCarb += recipe.carbs
            totalPro += recipe.protein
            totalFat += recipe.fat
            totalWat += recipe.water
            totalSod += recipe.sodium
            totalPho += recipe.phosphorus
            totalPot += recipe.potassium
            totalCal += recipe.calories
        
        #append the total to the actual lists (7 times to match the 7 days)
        proActList.append(totalPro)
        carbsActList.append(totalCarb)
        fatActList.append(totalFat)
        watActList.append(totalWat)
        sodActList.append(totalSod)
        phoActList.append(totalPho)
        potActList.append(totalPot)
        calActList.append(totalCal)
        

    #add selection ability using lists to send data
    selection = request.POST.get('nutList')
    actList = []
    nutrientList = []

    #if a user selects potassium, the lists pertaining to potassium will be sent as well as the 
    #variable of string showing what the user selected in the select box
    if selection == 'Potassium':
        nutrientList = potRecList
        actList = potActList
        nutSelectOpt = 'Potassium (mg)'
    elif selection == 'Carbs':
        nutrientList = carbsRecList
        actList = carbsActList
        nutSelectOpt = 'Carbs (g)'
    elif selection == 'Fat':
        nutrientList = fatRecList
        actList = fatActList
        nutSelectOpt = 'Fat (g)'
    elif selection == 'Sodium':
        nutrientList = sodRecList
        actList = sodActList
        nutSelectOpt = 'Sodium (mg)'
    elif selection == 'Phosphorus':
        nutrientList = phoRecList
        actList = phoActList
        nutSelectOpt = 'Phosphorous (mg)'
    elif selection == 'Calories':
        nutrientList = calRecList
        actList = calActList
        nutSelectOpt = 'Calories (kCal)'
    else :
        nutrientList = proRecList
        actList = proActList
        nutSelectOpt = 'Protein (g)'

    
    actListToPass = actList
    recListToPass = nutrientList


    history_meal_dict = Meal.objects.filter(user = user_id)


    context = {
        'user' : user,
        'history_meal_dict' : history_meal_dict,
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
        'pastWeekDates' : pastWeekDates,
        'actList' : actList,
        'recList' : nutrientList,
        'nutrientSelect' : nutSelectOpt

    }
    return render(request, 'health_app/history.html', context)

#this function is pertaining to the doughnut chart on the dash page
def pieChart(request) : 
    # user = User.objects.get(id = user_id)
    # today = datetime.now().date()
    # meal_dict = Meal.objects.filter(date = today, id= user_id)
    
    # recipe_list = list()
    # for meal in meal_dict :
    #     recipe_object = (Recipe.objects.get(id = meal.recipe.id))
    #     recipe_name = recipe_object.name
    #     recipe_list.append(recipe_name)
    data = Recipe.objects.all()
    data = ['Chicken', 'Egg', 'Milk']



    context = {
        'data' : data,
    }

    return render(request, 'health_app/piechart.html', context)

#after hitting an edit button, this sends the user to a page to edit a record 
def updateRecipePageView(request, user_id, meal_id):
    user = User.objects.get(id = user_id)
    meal = Meal.objects.get(id = meal_id, user = user_id)
    
    context = {
        'user' : user,
        'meal' : meal
    }
    return render(request, 'health_app/update_recipe.html', context)

#this allows people to edit their meals using on an edit page and then saves the changes
def editRecipe(request, user_id, meal_id):

    meal = Meal.objects.get(id = meal_id, user = user_id)
    meal.date = request.POST.get('meal_date')

    recipe = Recipe.objects.get(id = meal.recipe.id)
    recipe.name = request.POST.get('recipe_name')
    recipe.calories = request.POST.get('recipe_calories')
    recipe.carbs = request.POST.get('recipe_carbs')
    recipe.protein = request.POST.get('recipe_protein')
    recipe.fat = request.POST.get('recipe_fat')
    recipe.sodium = request.POST.get('recipe_sodium')
    recipe.phosphorus = request.POST.get('recipe_phosphorus')
    recipe.potassium = request.POST.get('recipe_potassium')
    recipe.water = request.POST.get('recipe_water')

    meal.save()
    recipe.save()

    return historyPageView(request, user_id)

#this allows a user to delete a food or recipe they recorded
def deleteRecipe(request, user_id, meal_id):
    meal = Meal.objects.get(id = meal_id, user = user_id)
    recipe = Recipe.objects.get(id = meal.recipe.id)
    meal.delete()
    recipe.delete()
    return historyPageView(request, user_id)

def nutritionPageView(request, user_id):
    user = User.objects.get(id = user_id)

    context = {
        'user' : user
    }
    return render(request, 'health_app/nutrition.html', context)