from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lab-rules/', views.lab_rules, name='lab-rules'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('experiment-lists/', views.exp_lists, name='exp-lists'),
]