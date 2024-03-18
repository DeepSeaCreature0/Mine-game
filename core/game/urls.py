from django.urls import path
from game.views import *

urlpatterns = [
    path("", input, name='input'), #url when starting the server
    path("index/<str:player1_name>/<str:player2_name>/<int:room_id>/", index, name='index'), #url to load game with given name and room id
    path("update/", update, name='update'), #url to update the win count of both player
]
