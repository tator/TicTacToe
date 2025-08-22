from game.engine import Engine
from game.engineBatch import EngineBatch
from players import *


if __name__ == "__main__":
    number = 100_000

    players = [
        PlayerRandom("Random1","X"),
        PlayerRandom("Random2","O")
    ]
    gameEngine = EngineBatch(players[0], players[1],number)
    gameEngine.play()

    players[0] = PlayerRandom("Random","X")
    players[1] = PlayerDumb("Dumb","O")
    gameEngine = EngineBatch(players[0], players[1],number)
    gameEngine.play()

    players[0] = PlayerDumb("Dumb1","x")
    players[1] = PlayerDumb("Dumb2","O")
    gameEngine = EngineBatch(players[0], players[1],number)
    gameEngine.play()