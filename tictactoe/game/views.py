import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Game


# Create your views here.
def index(request):
    return HttpResponse("Hello  world!")

def start_game(request):
    if request.method == 'GET':
        new_game = Game.objects.create()
        response_data = {
            'message': 'Game created, you can start as player X or O',
            'game': {
                'id': new_game.id,
                'board': new_game.board,
                'last_player': 'None',
            }
        }
        return JsonResponse(response_data, status=201)

@csrf_exempt
def play(request, game_id, player, position):
    if request.method == 'POST':
        game = get_object_or_404(Game, id = game_id)
        try:
            if game.is_finished:
                if game.winner == 'T':
                    return HttpResponse(f'This game is already over finished without a winner')
                else:
                    return HttpResponse(f'This game is already over, the winner was player {game.winner}')
            else:
                game.make_move(position, player)
                response_data = {
                    'message': game.check_status(),
                    'game': {
                        'id': game.id,
                        'board': game.board,
                        'last_player': game.last_player,
                    }
                }
                return JsonResponse(response_data, status=200)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        
def game_info(request, game_id):
    if request.method == 'GET':
        game = get_object_or_404(Game, id = game_id)
        response_data = {
            'message': game.check_status(),
            'game': {
                'id': game.id,
                'board': game.board,
                'last_player': game.last_player,
                'is_finished': game.is_finished,
                'winner': game.winner,
                }
            }
        return JsonResponse(response_data, status=200)

def get_all(request):
    if request.method == 'GET':
        games_list = Game.objects.all()
        games_json = []
        for game in games_list:
            game = {
                'id': game.id,
                'board': game.board,
                'last_player': game.last_player,
                'is_finished': game.is_finished,
                'winner': game.winner,
            }
            games_json.append(game)
        return JsonResponse(games_json, safe=False, status=200)