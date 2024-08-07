import pygame
from settings import Settings
from pygame.sprite import Sprite


class BabyBunny(Sprite):

    def __init__(self, ryo_carrot_game_object):
        super().__init__()

        self.initialize_landscape_settings(ryo_carrot_game_object)
        self.load_babybunny(ryo_carrot_game_object)
        self.start_position_babybunny()
        self.horizontal_position_babybunny()

    def initialize_landscape_settings(self, ryo_carrot_game_object):
        self.landscape = ryo_carrot_game_object.landscape
        self.settings = ryo_carrot_game_object.settings

    def load_babybunny(self, ryo_carrot_game_object):
        self.image = pygame.image.load('images/baby-bunny.png')
        self.image = pygame.transform.scale(self.image, (self.settings.babybunny_width,
                                                            self.settings.babybunny_height))
        self.rect = self.image.get_rect()

    def start_position_babybunny(self):
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def horizontal_position_babybunny(self):
        self.x = float(self.rect.x)
