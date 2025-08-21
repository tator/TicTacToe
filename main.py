from game import Engine
from players import PlayerHuman,PlayerRandom

if __name__ == "__main__":
    players = []
    players.append(PlayerHuman("Human","X"))
    players.append(PlayerRandom("AI","O"))
    gameEngine = Engine(players[0], players[1])
    gameEngine.play()