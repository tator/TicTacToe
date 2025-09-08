from .player import Player
from game import Board
from ai import AI
import numpy as np
import random
import os
import json

class AiPlayer(Player):

    def __init__(self, name, symbol, ai: AI):
        super().__init__(name,symbol)
        self.ai = ai
        
    def makeMove(self, board: Board):
        self.ai.setInput(board,self.symbol)
        self.ai.calulate()
        return self.ai.getOutput() + 1