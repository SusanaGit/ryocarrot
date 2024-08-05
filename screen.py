import pygame


class Screen:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.app_title = "Ryo Carrot Game"

        self.background_image = pygame.image.load('images/background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
