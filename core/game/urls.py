from django.urls import path
from game.views import *

urlpatterns = [
    path("", input, name='input'),
    path("index/<str:player1_name>/<str:player2_name>/<int:room_id>/", index, name='index'),
    path("update/", update, name='update'), 
]
