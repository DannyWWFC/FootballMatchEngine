class Team:
    def __init__(self, name: str, strength: int = 1):
        if strength < 0:
            raise ValueError("Strength cannot be negative")

        self.name = name
        self.strength = strength
        self.players = []

    def set_strength(self, strength: int):
        self.strength = strength

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def get_players_by_position(self, position):
        return [
            player
            for player in self.players
            if player.position == position
        ]

    def get_all_players(self):
        return players

    def __str__(self):
        return self.name