from django.urls import path
from MyApp import views

app_name = 'MyApp'

urlpatterns = [
    path('about/', views.index, name='about'),
]