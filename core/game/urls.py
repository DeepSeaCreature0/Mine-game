from django.urls import path, include
from game.views import *

urlpatterns = [
    path("", index),
]