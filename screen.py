import pygame


class Screen:

    def __init__(self):
        self.screen_width = None
        self.screen_height = None
        self.app_title = None
        self.background_image = None

    def initialize_screen(self):
        self.screen_width = 800
        self.screen_height = 800
        self.app_title = "Ryo Carrot Game"
        self.load_background_image()

    def initialize_screen_fullscreen(self):
        pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.app_title = "Ryo Carrot Game"
        self.load_background_image()

    def load_background_image(self):
        self.background_image = pygame.image.load('images/background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
