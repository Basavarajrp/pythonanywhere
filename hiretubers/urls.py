from django.urls import path


from . import views

urlpatterns = [
    path('hiretubers',views.hiretubers, name = 'hiretubers')
]
