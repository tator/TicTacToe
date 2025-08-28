from .player import Player
from game import Board
from ai import CreateNework
import numpy as np
import random
import os
import json

class AiPlayer(Player):

    def __init__(self, name, symbol):
        super().__init__(name,symbol)
        self.file = "ai/Network.json"
        if not os.path.exists(self.file):
            CreateNework.create()
        
        with open(self.file, "r") as f:
            data = json.load(f)

        self.input = np.array([]*9)
        self.w1 = np.array(data["w1"])
        self.b1 = np.array(data["b1"])
        self.w2 = np.array(data["w2"])
        self.b2 = np.array(data["b2"])
        self.w3 = np.array(data["w3"])
        self.b3 = np.array(data["b3"])
        self.output = np.array([])
    
    def setInput(self, board: Board):
        input = []
        for place in board.board:
            spot = 0
            if place == self.symbol:
                spot = 1.0
            elif not place == " " and not place == self.symbol:
                spot = -1.0
            input.append(spot)
        self.input = np.array(input)
    
    def relu(self,array):
        return np.maximum(0,array)
    
    def sigmoid(self,array):
        output = []
        for x in array:
            f = (1 / (1 + np.pow(np.e, -x)))
            output.append(f)
        return np.array(output)
    
    def pickMove(self,board: Board):
        sorted = np.argsort(self.output)[::-1]
        for index in sorted:
            if board.isValid(index + 1):
                return index + 1
        return None

    def makeMove(self, board: Board):
        self.setInput(board)
        n1 = np.dot(self.w1, self.input) + self.b1
        n1 = self.relu(n1)
        n2 = np.dot(self.w2, n1) + self.b2
        n2 = self.relu(n2)
        n3 = np.dot(self.w3, n2) + self.b3
        self.output = self.sigmoid(n3)
        choice = self.pickMove(board)
        return choice