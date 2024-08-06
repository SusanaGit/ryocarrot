import pygame


class Ryo:

    def __init__(self, ryo_carrot_game_object):
        self.landscape = None
        self.landscape_rect = None
        self.obtain_landscape_from_ryo_carrot_game(ryo_carrot_game_object)

        self.image_ryo = None
        self.rect_image_ryo = None
        self.load_image_ryo()

        self.moving_right_ryo = False
        self.moving_left_ryo = False

    def obtain_landscape_from_ryo_carrot_game(self, ryo_carrot_game_object):
        self.landscape = ryo_carrot_game_object.landscape
        self.landscape_rect = ryo_carrot_game_object.landscape.get_rect()

    def load_image_ryo(self):
        self.image_ryo = pygame.image.load('images/ryo.png')
        self.image_ryo = pygame.transform.scale(self.image_ryo, (100, 50))
        self.rect_image_ryo = self.image_ryo.get_rect()
        self.rect_image_ryo.midbottom = self.landscape_rect.midbottom

    def draw_ryo_current_location(self):
        self.landscape.blit(self.image_ryo, self.rect_image_ryo)

    def update_landscape(self, new_landscape):
        self.landscape = new_landscape
        self.landscape_rect = self.landscape.get_rect()

        self.rect_image_ryo.midbottom = self.landscape_rect.midbottom

    def update_position_ryo(self):
        if self.moving_right_ryo:
            self.rect_image_ryo.x += 1
        elif self.moving_left_ryo:
            self.rect_image_ryo.x -= 1