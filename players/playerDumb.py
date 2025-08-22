from .player import Player
from game.board import Board
import random

class PlayerDumb(Player):

    def makeMove(self, board: Board):
        if board.board[4] == " ":
            return 5
        if board.board[0] == " ":
            return 1
        if board.board[2] == " ":
            return 3
        if board.board[6] == " ":
            return 7
        if board.board[8] == " ":
            return 9
        if board.board[1] == " ":
            return 2
        if board.board[3] == " ":
            return 4
        if board.board[5] == " ":
            return 6
        if board.board[7] == " ":
            return 8        