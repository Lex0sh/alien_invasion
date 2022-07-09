import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблём"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение кораюля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom
        #sohranenie veshestvennoy koordinati centra korobla
        self.x = float(self.rect.x)

        # flag peremeshenia
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """obnovlaet poziciy koroblu s uchotom flaga"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #obnovlenie atributa rect na osnovanii self.x
        self. rect.x = self.x


    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """razmishaet korabl v centre nizhney storoni"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)