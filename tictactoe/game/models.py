from email import message
from django.db import models

# Create your models here.
class Game(models.Model):
    BOARD_SIZE = 9

    id = models.AutoField(primary_key=True)

    board = models.CharField(max_length=BOARD_SIZE, default='-' * BOARD_SIZE)

    last_player = models.CharField(max_length=1, choices=[('X', 'Player X'), ('O', 'Player O')], blank=True, null=True)

    is_finished = models.BooleanField(default=False)

    winner = models.CharField(max_length=1, choices=[('X', 'Player X'), ('O', 'Player O'), ('T', 'Tie')], blank=True, null=True)

    def __str__(self):
        return f'Game {self.id}: {self.board}'
    
    def  make_move(self, position,  player):
        
        if position < 0 or position > 8:
            raise ValueError("Position out of board")
        if  self.board[position] != '-':
            raise ValueError("This position is already choosed")
        if player not in  ['X', 'O'] or player == self.last_player:
            raise ValueError("Player must be different from the last one and X or O are the only options")
        if self.is_finished:
            raise ValueError("Game already finished")
        
        board_list = list(self.board)
        board_list[position] = player
        self.board = ''.join(board_list)
        self.last_player = player
        self.save()
    
    def check_status(self):

        board = self.board
        #Check column and rows

        for i in range(0,3):
            if board[0+i*3] == board[1+i*3] == board[2+i*3] != '-':
                self.winner = self.last_player
                self.is_finished = True
                self.save()
                return f'The game is over, winner is {self.winner}'
            if board[i] == board[i+3] == board[i+6] != '-':
                self.winner = self.last_player
                self.is_finished = True
                self.save()
                return f'The game is over, winner is {self.winner}'
            
        #Check diagonal
        
        if board[0] == board[4] == board[8] != '-' or board[2] == board[4] == board[6] != '-':
            self.winner = self.last_player
            self.is_finished = True
            self.save()
            return f'The game is over, winner is {self.winner}'
        
        #Check if tie
        
        if '-' not in board:
            self.winner = 'T'
            self.is_finished == True
            self.save()
            return f'The game is over, there is no winner'
        
        return f'The game must continue the last player was {self.last_player}'