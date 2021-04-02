from django.urls import path
from Search import views


app_name = "Search"


urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('history/', views.History.as_view(), name='history'),
     



]
