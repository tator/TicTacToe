from game.engine import Engine
from game.engineBatch import EngineBatch
from players import *


if __name__ == "__main__":
    players = []
    players.append(PlayerRandom("Random1","X"))
    players.append(PlayerRandom("Random2","O"))
    gameEngine = EngineBatch(players[0], players[1],1_000_000)
    gameEngine.play()

    players = []
    players.append(PlayerRandom("Random","X"))
    players.append(PlayerDumb("Dumb","O"))
    gameEngine = EngineBatch(players[0], players[1],1_000_000)
    gameEngine.play()