from django.urls import path

from . import views


urlpatterns = [
    path('', views.infoo, name='infoo')
]
