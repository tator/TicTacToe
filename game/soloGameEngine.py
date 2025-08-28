from .gameEngine import GameEngine
from players import Player

class SoloGameEngine(GameEngine):
    
    def __init__(self, player1: Player, player2: Player):
        super().__init__(player1, player2)

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

        
            

