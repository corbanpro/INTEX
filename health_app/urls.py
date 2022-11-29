from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView, dashboardRecipePageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashRecipe', dashboardRecipePageView, name= 'dashRecipe'),
    path('dash/', dashboardPageView, name= 'dash'),
    path('history/', historyPageView, name= 'history')
]                  
