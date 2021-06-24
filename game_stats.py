class GameStats:
    def __init__(self, my_game):
        self.setting=my_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left=self.settings.ship_limit