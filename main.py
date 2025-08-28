from game import *
from players import *


if __name__ == "__main__":
    number = 100_000

    players = [
        RandomPlayer("Random1","X"),
        RandomPlayer("Random2","O")
    ]
    gameEngine = BatchGameEngine(players[0], players[1],number)
    gameEngine.play()

    players[0] = RandomPlayer("Random","X")
    players[1] = DumbPlayer("Dumb","O")
    gameEngine = BatchGameEngine(players[0], players[1],number)
    gameEngine.play()
