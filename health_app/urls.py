from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView, dashboardRecipePageView, registerPageView, loginPageView, addRecipePageView, addIngredientPageView, dashboardIngredientPageView, dashboardIngredientUnitPageView, dashboardUserPageView, addWaterPageView, dashboardLoginPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashIngredient/<str:user>', dashboardIngredientPageView, name= 'dashIngredient'),
    path('dashRecipe/<str:user>', dashboardRecipePageView, name= 'dashRecipe'),
    path('dashUser/', dashboardUserPageView, name='dashUser'),
    path('dash/', dashboardPageView, name= 'dash'),
    path('history/', historyPageView, name= 'history'),
    path('addRecipe/<str:user>', addRecipePageView, name= 'addRecipe'),
    path('register/', registerPageView, name= 'register'),
    path('login/', loginPageView, name = 'login'),
    path('ingredientUnit/<str:user>', dashboardIngredientUnitPageView, name= 'ingredientUnit'),  
    path('addIngredient/<int:ingredient_id><str:user>', addIngredientPageView, name= 'addIngredient'),
    path('addWater/<str:user>', addWaterPageView, name= 'addWater'),
    path('dashLogin/', dashboardLoginPageView, name= 'dashLogin'),


]                  
