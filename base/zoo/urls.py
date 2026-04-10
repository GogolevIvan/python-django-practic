from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/<int:animal_id>', views.get_animal, name='single_animal'),
]