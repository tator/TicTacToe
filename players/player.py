from abc import ABC, abstractmethod
from game.board import Board

class Player(ABC):
    
    def __init__(self, name,symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def makeMove(self, board: Board):
        pass