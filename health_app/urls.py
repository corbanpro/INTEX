from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dash/', dashboardPageView, name= 'dash'),
    path('history/', historyPageView, name= 'history')
]                  
