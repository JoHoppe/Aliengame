class GameStats():
    """tracks game stats"""
    def __init__(self,settings):
        self.settings=settings
        self.reset_stats()
        """active game flag"""
        self.game_active = True

    def reset_stats(self):
        """tracks varible stats"""
        self.ship_lives=self.settings.ship_lives

