from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns = [
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    
    
    #we cannot have logout as view function because django comes
    #with in built logout method, so for end_point and for name we can have as logout.
    path('logout',views.logout_user, name="logout"),
    path('dashboard',views.dashboard, name="dashboard"),
    
    ]