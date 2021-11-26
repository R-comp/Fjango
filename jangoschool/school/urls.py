from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path(r'score/',showscore,name='showscore'),
    path(r'register/',register,name='register')
]