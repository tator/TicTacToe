from game.engine import Engine
from players.playerHuman import PlayerHuman
from players.playerRandom import PlayerRandom

if __name__ == "__main__":
    players = []
    players.append(PlayerHuman("Human","X"))
    players.append(PlayerRandom("AI","O"))
    gameEngine = Engine(players[0], players[1])
    gameEngine.play()