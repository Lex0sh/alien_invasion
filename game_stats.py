class GameStats():
    """otslezhevanie statistiki dlya igri"""

    def __init__(self, ai_game):
        """inicializiruet statistiku"""
        self.settings = ai_game.settings
        self.reset_stats()
        # igra zapuskaetsya v neaktivnom rezhime 
        self.game_active = False

        # record ne dolzhen sbrasivatsya
        self.high_score = 0


    def reset_stats(self):
        """inicializiruet statistiku izmenyaushuyusya v hode igri"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1