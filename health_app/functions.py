sawyer_api_key = '04fb037d86mshbc10cd2bcf9efc3p1b1aa2jsnb5518a2797b1' #Sawyer's API key
toph_api_key = 'ffcbb1d69amsh90230347f7931d3p1536aejsn25568159361e'
api_key = toph_api_key

def searchRecipes(recipe):
    import requests
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
    querystring = {"query":[recipe], #this is the only required parameter. It is what will be entered in the 'search bar'.
                "number":"2"
    }
    headers = {
        "X-RapidAPI-Key": "04fb037d86mshbc10cd2bcf9efc3p1b1aa2jsnb5518a2797b1",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    responseSearchRecipe = requests.request("GET", url, headers=headers, params=querystring)
    r = responseSearchRecipe.json()
    #Make a dictionary with the recipe name as the key and the recipe ID as the value
    recipeDict = {}
    for i in r['results']:
        recipeDict[i['title']] = i['id']
    
    return(recipeDict)


#@title Get Recipe Information
def getRecipeInformation(id):
    #The desired ID is then put into another API call to the endpoint GetRecipeInformation
    recipeID = id #change this once we get another input
    recipeID = str(recipeID)

    import requests

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipeID}/information"

    querystring = {"includeNutrition":"true"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    responseGetRecipeInformation = requests.request("GET", url, headers=headers, params=querystring)

    #make a dictionary with the required nutrients
    r = responseGetRecipeInformation.json()
    nutrientDict = {}
    nutrientDict['title'] = r['title']
    nutrientDict['fat'] = r['nutrition']['nutrients'][1]['amount']
    nutrientDict['protein'] = r['nutrition']['nutrients'][8]['amount']
    nutrientDict['carbs'] = r['nutrition']['nutrients'][3]['amount']
    nutrientDict['potassium'] = r['nutrition']['nutrients'][17]['amount']
    nutrientDict['phosphorus'] = r['nutrition']['nutrients'][14]['amount']
    nutrientDict['sodium'] = r['nutrition']['nutrients'][7]['amount']
    nutrientDict['calories'] = r['nutrition']['nutrients'][0]['amount']
    
    return nutrientDict


#@title Search Ingredients
def searchIngredients(ingredient):
    import requests
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/search"
    querystring = {"query":[ingredient],"number":"2"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    responseSearchIngredients = requests.request("GET", url, headers=headers, params=querystring)
    r = responseSearchIngredients.json()
    #Make a dictionary with the recipe name as the key and the recipe ID as the value
    ingredientDict = {}
    for i in r['results']:
        ingredientDict[i['name']] = i['id']
    
    return(ingredientDict)


#@title Get Ingredient Information 1
#There are two API calls for getIngredientInformation. The first one will use the ingredient ID to return suggested Units. 
#The user must input an amount and a unit to get the correct nutrient information. 
def getIngredientInformation1(id):
    import requests

    ingredientID = id #change this once we get another input
    ingredientID = str(ingredientID)

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/{ingredientID}/information"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    responseGetIngredientInformation1 = requests.request("GET", url, headers=headers)
    r = responseGetIngredientInformation1.json()
    #make a dictionary with the possible units
    unitList = []
    for i in r['possibleUnits']:
        unitList.append(i)

    return unitList


#@title Get Ingredient Information 2
#Using the units from Get Ingredient Information 2, display 

def getIngredientInformation2(id, amount, unit):
    import requests
    ingredientID = id #change this once we get another input
    ingredientID = str(ingredientID)

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/{ingredientID}/information"

    querystring = {"amount":{amount},"unit":{unit}}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    responseGetIngredientInformation2 = requests.request("GET", url, headers=headers, params=querystring)
    r = responseGetIngredientInformation2.json()

    nutrientDict = {}
    nutrientDict['name'] = r['name']
    nutrientDict['fat'] = r['nutrition']['nutrients'][1]['amount']
    nutrientDict['protein'] = r['nutrition']['nutrients'][9]['amount']
    nutrientDict['carbs'] = r['nutrition']['nutrients'][24]['amount']
    nutrientDict['potassium'] = r['nutrition']['nutrients'][15]['amount']
    nutrientDict['phosphorus'] = r['nutrition']['nutrients'][16]['amount']
    nutrientDict['sodium'] = r['nutrition']['nutrients'][19]['amount']
    nutrientDict['calories'] = r['nutrition']['nutrients'][30]['amount']
    return nutrientDict

