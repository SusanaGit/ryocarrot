import pygame
import random

from pygame.sprite import Sprite


class BabyBunny(Sprite):

    def __init__(self, ryo_carrot_game_object):
        super().__init__()

        self.initialize_landscape_settings(ryo_carrot_game_object)
        self.load_babybunny()
        self.start_position_babybunny()
        self.x_position_babybunny()
        self.y_position_babybunny()

    def initialize_landscape_settings(self, ryo_carrot_game_object):
        self.landscape = ryo_carrot_game_object.landscape
        self.settings = ryo_carrot_game_object.settings

    def load_babybunny(self):
        self.image = pygame.image.load('images/baby-bunny.png')
        self.image = pygame.transform.scale(self.image, (self.settings.babybunny_width,
                                                         self.settings.babybunny_height))
        self.rect = self.image.get_rect()

    def start_position_babybunny(self):
        info = pygame.display.Info()
        random_number_x = random.randrange(0, (info.current_w - self.rect.width))
        self.rect.x = random_number_x
        self.rect.y = 0

    def x_position_babybunny(self):
        self.x = float(self.rect.x)

    def y_position_babybunny(self):
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.babybunny_speed
        self.rect.y = self.y