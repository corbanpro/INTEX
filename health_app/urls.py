from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView, dashboardRecipePageView, registerPageView, loginPageView, addRecipePageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashRecipe', dashboardRecipePageView, name= 'dashRecipe'),
    path('dash/', dashboardPageView, name= 'dash'),
    path('history/', historyPageView, name= 'history'),
    path('addRecipe/<int:userID>', addRecipePageView, name= 'addRecipe'),
    path('register/', registerPageView, name= 'register'),
    path('login/', loginPageView, name = 'login')
]                  
