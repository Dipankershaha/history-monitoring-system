from django.urls import path
from Login import views


app_name = "Login"


urlpatterns = [
     path('signup/', views.sign_up, name='sign_up'),
     path('login/', views.login_page, name='login'),
     path('edit/', views.edit_profile, name='edit'),
     path('logout/', views.logout_user, name='logout'),
    #  path('auto_register10/',views.auto_register10, name='auto_register10'),
    #  path('profile/', views.profile, name='profile'),
    #  path('user/<username>/', views.user, name='user'),
    



]
