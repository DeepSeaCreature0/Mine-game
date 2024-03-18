from django.shortcuts import render, redirect
from .models import Game
from django.http import JsonResponse

def input(request):
    error_message = None  
    
    if request.method == 'POST':
        player1_name = request.POST.get('player1')
        player2_name = request.POST.get('player2')
        room_id = request.POST.get('room_id')
        
        # Check if a game with the same room ID already exists
        if Game.objects.filter(room_id=room_id).exists():
            error_message = 'A game with the same Room ID already exists.'
        else:
            # Create the game object
            game = Game.objects.create(player1=player1_name, player2=player2_name, room_id=room_id)
            game.save()
            
            # Redirect to index page with player names
            return redirect('index', player1_name=player1_name, player2_name=player2_name, room_id=room_id)
    
    return render(request, 'input.html', {'error_message': error_message})


def index(request, player1_name, player2_name,room_id):
    return render(request, 'index.html', {'player1_name': player1_name, 'player2_name': player2_name, 'room_id':room_id})

def update(request):
    if request.method == 'POST':
        winner = request.POST.get('winner')
        room_id = request.POST.get('room_id')
        print("Winner:"+winner)
        game = Game.objects.get(room_id=room_id)
        if winner == 'player1':
            game.player1wins += 1
        elif winner == 'player2':
            game.player2wins += 1
        game.save()
        player1_name=game.player1
        player2_name=game.player2
        return redirect('index', player1_name=player1_name, player2_name=player2_name, room_id=room_id)
