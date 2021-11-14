from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('score/',showscore,name='showscore'),
    path('register/',register,name='register')
]