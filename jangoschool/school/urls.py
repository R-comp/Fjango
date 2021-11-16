from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('score/',showscore,name='showscore'),
    path('register/',register,name='register')
]