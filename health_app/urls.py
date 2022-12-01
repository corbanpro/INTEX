from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView, dashboardRecipePageView, registerPageView, loginPageView, addRecipePageView, addIngredientPageView, dashboardIngredientPageView, dashboardIngredientUnitPageView, dashboardUserPageView, addWaterPageView, dashboardLoginPageView, updateRecipePageView, editRecipe, deleteRecipe, nutritionPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashIngredient/<int:user_id>', dashboardIngredientPageView, name= 'dashIngredient'),
    path('dashRecipe/<int:user_id>', dashboardRecipePageView, name= 'dashRecipe'),
    path('dashUser/', dashboardUserPageView, name='dashUser'),
    path('dash/<int:user_id>', dashboardPageView, name= 'dash'),
    path('dash/<int:user_id>/<str:recipe_name>/<str:ingredient_name>/<int:ingredient_id>/<str:selection>', dashboardPageView, name= 'dash'),
    path('history/<int:user_id>', historyPageView, name= 'history'),
    path('addRecipe/<int:user_id>', addRecipePageView, name= 'addRecipe'),
    path('register/', registerPageView, name= 'register'),
    path('login/', loginPageView, name = 'login'),
    path('ingredientUnit/<int:user_id>/<str:ingredient_name>', dashboardIngredientUnitPageView, name= 'ingredientUnit'),  
    path('addIngredient/<int:ingredient_id>/<int:user_id>/<str:ingredient_name>', addIngredientPageView, name= 'addIngredient'),
    path('addWater/<int:user_id>', addWaterPageView, name= 'addWater'),
    path('dashLogin/', dashboardLoginPageView, name= 'dashLogin'),
    path('update/<int:user_id>/<int:meal_id>', updateRecipePageView, name='update_recipe'),
    path('edit/<int:user_id>/<int:meal_id>', editRecipe, name="edit_recipe"),
    path('delete/<int:user_id>/<int:meal_id>', deleteRecipe, name="delete_recipe"),
    path('nutrition/<int:user_id>', nutritionPageView, name="nutrition")
    # path('dashPie/', pieChart, name='pieChart' )

]                  
