import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """klass dla upravlenia snaradami"""

    def __init__(self, ai_game):
        """sozdayt object snaradov v tekushey pozicii koroblya"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #sozdanie snaryasda v pozicii 0 0 i naznachenii pravilnoy pozicii
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #poziciya snaryada hranitsya v veshestvennom formate
        self.y = float(self.rect.y)

    def update(self):
        """peremeshaet snaryad vversch po ekranu"""
        #obnovlenie pozicii snaryda v veshestvennom formate
        self.y -= self.settings.bullet_speed
        #obnovlenie pozicii pryamougolnika
        self.rect.y = self.y

    def draw_bullet(self):
        """vivod snaryada na ekran"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        