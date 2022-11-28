from django.urls import path
from .views import indexPageView, dashboardPageView, historyPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path('dashboard/', dashboardPageView, name= 'dashboard'),
    path('history/', historyPageView, name= 'history')
]                  
