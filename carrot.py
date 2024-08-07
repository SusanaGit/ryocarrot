import pygame
from pygame.sprite import Sprite


class Carrot(Sprite):

    def __init__(self, ryo_carrot_game_object):
        super().__init__()

        self.initialize_landscape_settings(ryo_carrot_game_object)

        self.load_carrot(ryo_carrot_game_object)

        self.decimal_value_position_carrot()

    def initialize_landscape_settings(self, ryo_carrot_game_object):
        self.landscape = ryo_carrot_game_object.landscape
        self.settings = ryo_carrot_game_object.settings

    def load_carrot(self, ryo_carrot_game_object):
        self.image_carrot = pygame.image.load('images/carrot.png')
        self.image_carrot = pygame.transform.scale(self.image_carrot, (self.settings.carrot_width,
                                                                       self.settings.carrot_height))
        self.rect = self.image_carrot.get_rect()
        self.rect.midtop = ryo_carrot_game_object.ryo.rect.midtop

    def decimal_value_position_carrot(self):
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.carrot_speed
        self.rect.y = self.y

    def draw_carrot(self):
        self.landscape.blit(self.image_carrot, self.rect)