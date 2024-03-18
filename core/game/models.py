from django.db import models

# Create your models here.
class Game(models.Model):
    room_id=models.PositiveIntegerField(unique=True)
    player1=models.CharField(max_length=100)
    player2=models.CharField(max_length=100)
    player1wins=models.PositiveIntegerField(default=0)
    player2wins=models.PositiveIntegerField(default=0)