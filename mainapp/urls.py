from django.urls import path

from mainapp.views import *

urlpatterns = [
    path('', main, name='main'),
    path('mazda', car_mazda, name='mazda'),
    path('audi', car_audi, name='audi'),
    path('bmw', car_bmw, name='bmw'),
]