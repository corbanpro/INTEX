from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView, dashboardRecipePageView, registerPageView, loginPageView, addRecipePageView, addIngredientPageView, dashboardIngredientPageView, dashboardIngredientUnitPageView, dashboardUserPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashRecipe', dashboardRecipePageView, name= 'dashRecipe'),
    path('dashUser', dashboardUserPageView, name='dashUser'),
    path('dash/', dashboardPageView, name= 'dash'),
    path('history/', historyPageView, name= 'history'),
    path('addRecipe/', addRecipePageView, name= 'addRecipe'),
    path('register/', registerPageView, name= 'register'),
    path('login/', loginPageView, name = 'login'),
    path('dashIngredient/', dashboardIngredientPageView, name= 'dashIngredient'),
    path('ingredientUnit/', dashboardIngredientUnitPageView, name= 'ingredientUnit'),  
    path('addIngredient/<int:ingredient_id>', addIngredientPageView, name= 'addIngredient'),


]                  
