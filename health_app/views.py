from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'health_app/index.html')

def dashboardPageView(request) :
    return render(request, 'health_app/dash.html')

def historyPageView(request) :
    return render(request, 'health_app/history.html')




