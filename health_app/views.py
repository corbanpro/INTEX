from django.shortcuts import render
from .functions import searchRecipes


def indexPageView(request) :
    # recipe_name = request.GET['recipe_name']
    # returned_recipes = searchRecipes(recipe_name)    
    # context = {
    #         'recipes' : returned_recipes['Chicken Quesadilla']
    #     }

    return render(request, 'health_app/index.html')

    # else: 
    #     return render(request, 'health_app/index.html')



def dashboardPageView(request) :
    return render(request, 'health_app/dash.html')

def historyPageView(request) :
    return render(request, 'health_app/history.html')




