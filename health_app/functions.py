def searchRecipes(recipe):
<<<<<<< HEAD
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
=======
    pass
#     import requests
#     url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
#     querystring = {"query":[recipe], #this is the only required parameter. It is what will be entered in the 'search bar'.
#                 "number":"2"
#     }
#     headers = {
#         "X-RapidAPI-Key": "04fb037d86mshbc10cd2bcf9efc3p1b1aa2jsnb5518a2797b1",
#         "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
#     }
#     responseSearchRecipe = requests.request("GET", url, headers=headers, params=querystring)
#     r = responseSearchRecipe.json()
#     #Make a dictionary with the recipe name as the key and the recipe ID as the value
#     recipeDict = {}
#     for i in r['results']:
#         recipeDict[i['title']] = i['id']
>>>>>>> 3bf557d (css hopefully)
    
    return(recipeDict)

<<<<<<< HEAD
=======

# print(searchRecipes('chicken quesadilla'))
>>>>>>> 3bf557d (css hopefully)
