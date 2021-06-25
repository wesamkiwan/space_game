class GameStats:
    def __init__(self,my_game):
        self.settings=my_game.settings
        self.reset_stats()
        self.game_active=True
        
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit