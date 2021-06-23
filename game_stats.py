from space_game import SpaceGame


class GameStats:
    def __init__(self, SpaceGame):
        self.setting=SpaceGame.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left=SpaceGame.settings.ship_limit