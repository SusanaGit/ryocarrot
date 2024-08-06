import pygame
from pygame.sprite import Sprite

class Carrot(Sprite):

    def __init__(self, ryo_carrot_game_object):
        super().__init__()
        self.initialize_landscape_settings(ryo_carrot_game_object)

    def initialize_landscape_settings(self, ryo_carrot_game_object):
        self.landscape = ryo_carrot_game_object.landscape
        self.settings = ryo_carrot_game_object.settings
        self.color_carrot = self.settings.carrot_color

    def create_carrot(self, ryo_carrot_game_object):
        self.rect_carrot = pygame.Rect(0, 0, self.settings.carrot_width,
                                       self.settings.carrot_height)
        self.rect_carrot.midtop = ryo_carrot_game_object.ryo.rect_image_ryo.midtop

