from player import Player

class Game:
    def __init__(self):
        self.round = 0
        self.players = []
        self.current_player = 0
        self.action_points = 2

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.round += 1
        self.current_player += 1
        self.action_points = 2

