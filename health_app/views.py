from django.shortcuts import render
from .functions import searchRecipes


def indexPageView(request) :
    context = {
        'recipedict' : searchRecipes('chicken quesadilla')
    }
    return render(request, 'health_app/index.html', context)



def dashboardPageView(request) :
    context = {
        'recipe_dict' : {}
    }

    return render(request, 'health_app/dash.html', context)

def dashboardRecipePageView(request) :
    recipe_name = request.GET['recipe_name']
    context = {
        'recipe_dict' : searchRecipes(recipe_name)
    }

    return render(request, 'health_app/dash.html', context)

def addRecipePageView(request) :
    # add recipe
    context = {

    }

    return render(request, 'health_app/dash.html', context)



def historyPageView(request) :
    return render(request, 'health_app/history.html')




