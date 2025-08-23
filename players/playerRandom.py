from .player import Player
from game import Board
import random

class PlayerRandom(Player):

    def makeMove(self, board: Board):
        return random.randint(1, 9)