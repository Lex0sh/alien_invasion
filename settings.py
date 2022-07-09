class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """inicializiruet staticheskie nastroyki iggri"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #nastroiki korobla
        self.ship_speed = 2.5
        self.ship_limit = 3
        #parametri snaryda
        self.bullet_speed = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #nastroyki prishelcev
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleep_directeon = 1 oboznachaet dvizhenie vpravo; a -1 vlevo
        self.fleet_direction = 1
        # temp uskoreniya igri
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """inicializiruet nastroyki izmenyaushiesya v hode igri"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_derection = 1 oboznachaet dvizhenie vpravo; a = -1 vlevo
        self.fleet_direction = 1
        # podschet ochkov
        self.alien_points = 50

    def increase_speed(self):
        """ uvelichivaet nastroyki skorosti"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)