from game.board import Board
from players.player import Player

class Engine:
    
    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.board = Board()
        self.currentTurn = 0

    def nextTurn(self):
        self.currentTurn = 1 - self.currentTurn

    def checkWinner(self):
        b = self.board.board
        winPositions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for pos in winPositions:
            if b[pos[0]] == b[pos[1]] == b[pos[2]] != " ":
                return True
        return False

    def play(self):
        while not self.board.isFull():
            player = self.players[self.currentTurn]
            move = player.makeMove(self.board)
            if self.board.updateBoard(move,player.symbol):
                print(f"{player.name} moves to {move}")
                if self.checkWinner():
                    self.board.display()
                    print(f"{player.name} wins!")
                    return
                self.nextTurn()
        self.board.display()
        print("It's a tie!")

        
            

