from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.get_random, name='random')
]