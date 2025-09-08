from abc import ABC,abstractmethod
from game import Board

class AI(ABC):
    def __init__(self):
        print()

    @abstractmethod
    def setInput(self, board: Board, playerSymbol):
        pass

    @abstractmethod
    def calulate(self):
        pass

    @abstractmethod
    def getOutput(self):
        pass