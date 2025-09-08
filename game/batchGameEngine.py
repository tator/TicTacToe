import sys
import time
from .gameEngine import GameEngine
from players import Player



class BatchGameEngine(GameEngine):
    
    def __init__(self, player1: Player, player2: Player, number: int, biDirection = True):
        super().__init__(player1,player2)
        self.mainPlayer = player1
        self.number = number
        self.stats = {"sym": self.mainPlayer.symbol, "wins": 0, "losses": 0, "ties": 0, "time": 0}
        self.elapsed_time = 0
        self.biDirection = biDirection

    def statReset(self):
        self.stats = {"sym": self.mainPlayer.symbol, "wins": 0, "losses": 0, "ties": 0, "time": 0}
    
    def printTitle(self):
        print()
        print(f"{self.players[0].name} playing {self.number:,} games aganst {self.players[1].name}")
        print()
        print(f"{'Symbol':<15} | {'Wins %':<8} {'Losses %':<10} {'Ties %':<8} | {'Time(sec)':<10}")
        print("-"*16 + "|" + "-"*30 + "|"+"-"*10)

    def printStats(self):
        name = f"{self.mainPlayer.name} as {self.stats['sym']}:"
        total_games = self.stats['wins'] + self.stats['losses'] + self.stats['ties']
        if total_games == 0:
            wins = losses = ties = 0
        else:
            wins = (self.stats['wins'] / total_games) * 100
            losses = (self.stats['losses'] / total_games) * 100
            ties = (self.stats['ties'] / total_games) * 100
        print(f"{name:<15} | {wins:<8.1f} {losses:<10.1f} {ties:<8.1f} | {self.stats['time']:.4f}")
        
    def loading_bar(self, current, total, length=46):
        percent = current / total
        filled = int(length * percent)
        bar = "█" * filled + "-" * (length - filled)
        sys.stdout.write(f"\r|{bar}| {percent:.0%}")
        sys.stdout.flush()

    def playOne(self):
        while not self.board.isFull():
            player = self.players[self.currentTurn]
            move = player.makeMove(self.board)
            if self.board.updateBoard(move, player.symbol):
                if self.checkWinner():
                    break
                self.nextTurn()
        if self.board.isFull():
            self.stats["ties"] += 1
            return
        if self.players[self.currentTurn] == self.mainPlayer:
            self.stats["wins"] += 1
        else:
            self.stats["losses"] += 1

    def loop(self,turn = 0):
        start_time = time.time()
        counter = 0
        while counter < self.number:
            self.currentTurn = 0
            if counter % (self.number / 100) == 0:
                self.loading_bar(counter, self.number)
            self.playOne()
            self.board.reset()
            counter += 1
        self.loading_bar(counter, self.number)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.stats["time"] = elapsed_time
        sys.stdout.write("\r" + " " * 60 + "\r")
        sys.stdout.flush()

    def play(self):
        self.printTitle()
        self.loop()
        self.printStats()
        if(self.biDirection):
            self.players.reverse()
            self.players[0].symbol = "X"
            self.players[1].symbol = "O"
            self.statReset()
            self.loop()
            self.printStats()
        print()



        
            

