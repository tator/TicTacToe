import sys
from game.board import Board
from players.player import Player


class EngineBatch:
    
    def __init__(self, player1: Player, player2: Player, number: int):
        self.players = [player1, player2]
        self.board = Board()
        self.currentTurn = 0
        self.number = number
        self.stats = {
            self.players[0].name: {"wins": 0, "losses": 0, "ties": 0},
            self.players[1].name: {"wins": 0, "losses": 0, "ties": 0}
        }

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
    
    def printStats(self):
        print()
        print()
        print(f"{'Player':<10} {'Wins %':<8} {'Losses %':<10} {'Ties %':<8}")
        print("-" * 40)
        for player, record in self.stats.items():
            total_games = record['wins'] + record['losses'] + record['ties']
            if total_games == 0:
                wins = losses = ties = 0
            else:
                wins = (record['wins'] / total_games) * 100
                losses = (record['losses'] / total_games) * 100
                ties = (record['ties'] / total_games) * 100
            print(f"{player:<10} {wins:<8.1f} {losses:<10.1f} {ties:<8.1f}")
        print()

    def loading_bar(self, current, total, length=30):
        percent = current / total
        filled = int(length * percent)
        bar = "█" * filled + "-" * (length - filled)
        sys.stdout.write(f"\r|{bar}| {percent:.0%}")
        sys.stdout.flush()

    def play(self):
        counter = 0
        while counter < self.number:
            self.currentTurn = counter % 2
            if counter % (self.number / 100) == 0:
                self.loading_bar(counter, self.number)
            while not self.board.isFull():
                player = self.players[self.currentTurn]
                move = player.makeMove(self.board)
                if self.board.updateBoard(move,player.symbol):
                    if self.checkWinner():
                        self.stats[player.name]["wins"] += 1
                        self.stats[self.players[1 - self.currentTurn].name]["losses"] += 1
                        break
                    self.nextTurn()
            if self.board.isFull():
                self.stats[self.players[0].name]["ties"] += 1
                self.stats[self.players[1].name]["ties"] += 1
            self.board.reset()
            counter += 1
        self.loading_bar(counter, self.number)
        self.printStats()


        
            

