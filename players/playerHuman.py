from players.player import Player
from game.board import Board

class PlayerHuman(Player):

    def makeMove(self, board):
        self.displayOptions(board)
        move = int(input(f"{self.name}, enter your move: "))
        return move
    
    def displayOptions(self,board: Board):
        displayBoard = []
        for i, cell in enumerate(board.board):
            if cell == ' ':
                displayBoard.append(str(i + 1))  # show position number for empty cells
            else:
                displayBoard.append(cell)
        
        for i in range(0, 9, 3):
            print(f" {displayBoard[i]} | {displayBoard[i+1]} | {displayBoard[i+2]} ")
            if i < 6:
                print("---+---+---")