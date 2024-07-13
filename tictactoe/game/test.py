
from django.test import TestCase, Client
from django.urls import reverse

from .models import Game


class GameTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_start_game(self):
        response = self.client.get(reverse('start_game'))
        self.assertEqual(response.status_code, 201)
        self.assertIn('game', response.json())
        self.assertIn('id', response.json()['game'])

    def test_play_view(self):
        game = Game.objects.create()
        url = reverse('play', args=[game.id, 'X', 0])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('game', response.json())
        self.assertEqual(response.json()['game']['board'][0], 'X')

    def test_game_info_view(self):
        game = Game.objects.create()
        url = reverse('game_info', args=[game.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('game', response.json())
        self.assertEqual(response.json()['game']['id'], game.id)

    def test_make_move_position_already_chosen(self):
        game = Game.objects.create()
        url = reverse('play', args=[game.id, 'X', 0])
        self.client.post(url)
        response = self.client.post(url.replace('X', 'O'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], "This position is already choosed")

    def test_make_move_invalid_player(self):
        game = Game.objects.create()
        url = reverse('play', args=[game.id, 'Invalid', 0])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], "Player must be different from the last one and X or O are the only options")

    def test_make_move_out_of_board_position(self):
        game = Game.objects.create()
        url = reverse('play', args=[game.id, 'X', 10])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], "Position out of board")

    def test_check_status_winner_column(self):
        game = Game.objects.create()
        game.board = 'XO-XO-X--'
        game.last_player = 'X'
        game.check_status()
        url = reverse('game_info', args=[game.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['game']['is_finished'])
        self.assertEqual(response.json()['game']['winner'], 'X')
    
    def test_check_status_game_continues(self):
        game = Game.objects.create()
        game.board = 'X--------'
        game.last_player = 'X'
        game.save()
        url = reverse('game_info', args=[game.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'The game must continue the last player was X')