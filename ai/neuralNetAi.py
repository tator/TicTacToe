from .ai import AI
from game import Board
import numpy as np
import random

class NeuralNetAi(AI):
    def __init__(self,networkShape = [9, 36, 36, 9]):
        self.networkShape = networkShape
        self.input = np.empty(networkShape[0])
        self.w = [np.empty((networkShape[i+1], networkShape[i])) for i in range(len(networkShape)-1)]
        self.b = [np.empty((networkShape[i+1])) for i in range(len(networkShape)-1)]
        self.output = np.empty(networkShape[len(networkShape)-1])
        
        

    def randomInit(self):
        self.w = [np.random.randn(self.networkShape[i+1], self.networkShape[i]) for i in range(len(self.networkShape)-1)]
        self.b = [np.random.randn(self.networkShape[i+1]) for i in range(len(self.networkShape)-1)]

    def setInput(self, board: Board, playerSymbol):
        input = []
        for place in board.board:
            if place == playerSymbol:
                input.append(1.0)
            elif not place == " " and not place == playerSymbol:
                input.append(-1.0)
            else:
                input.append(0.0)
        self.input = np.array(input)
        #print()
        #print(f"setInput{self.input}")

    def calulate(self):
        nodeLayer = self.input
        count = 0 
        while count < len(self.networkShape)-1:
            out = np.dot(self.w[count], nodeLayer) + self.b[count]
            if count != len(self.networkShape) - 1:
                nodeLayer = self.sigmoid(out)
            else:
                nodeLayer = self.relu(out)
            count += 1
        self.output = nodeLayer

    def getOutput(self):
        sorted = np.argsort(self.output)[::-1]
        #print(self.output)
        #print(sorted)
        for index in sorted:
            if self.input[index] == 0.0:
                return index
        return None
    
    def relu(self,array):
        return np.maximum(0,array)
    
    def sigmoid(self,array):
        output = []
        for x in array:
            f = (1 / (1 + np.pow(np.e, -x)))
            output.append(f)
        return np.array(output)
    
    def createChild(self,mutationRate,mutation ):
        return
    

