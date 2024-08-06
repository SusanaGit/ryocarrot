import sys
import pygame

from ryo import Ryo
from screen import Screen


class RyoCarrotGame:
    def __init__(self):
        pygame.init()

        self.screen = Screen()
        self.landscape = None
        self.is_fullscreen = False
        self.countChangeSizeLandscape = 0

        self.initialize_screen()
        self.ryo = Ryo(self)

    def run_ryo_carrot_game(self):
        running = True

        while running:

            self.choose_events()

            self.ryo.update_position_ryo()

            self.update_landscape()

    def choose_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.change_size_screen()
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.ryo.moving_right_ryo = True
                elif event.key == pygame.K_LEFT:
                    self.ryo.moving_left_ryo = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ryo.moving_right_ryo = False
                if event.key == pygame.K_LEFT:
                    self.ryo.moving_left_ryo = False

    def update_landscape(self):
        self.landscape.blit(self.screen.background_image, (0, 0))
        self.ryo.draw_ryo_current_location()
        pygame.display.flip()

    def initialize_screen(self):
        self.screen.initialize_screen()
        self.landscape = pygame.display.set_mode(
            (self.screen.screen_width,
             self.screen.screen_height)
        )
        pygame.display.set_caption(self.screen.app_title)

    def change_size_screen(self):
        if self.countChangeSizeLandscape % 2 == 0:
            self.screen.initialize_screen_fullscreen()
            self.landscape = pygame.display.set_mode(
                (self.screen.screen_width,
                 self.screen.screen_height),
                pygame.FULLSCREEN
            )
            print("landscape fullscreen: ", self.screen.screen_width)
            print("landscape fullscreen: ", self.screen.screen_height)
            self.countChangeSizeLandscape += 1
            self.is_fullscreen = True
        else:
            self.screen.initialize_screen()
            self.landscape = pygame.display.set_mode(
                (self.screen.screen_width,
                 self.screen.screen_height)
            )
            print("landscape: ", self.screen.screen_width)
            print("landscape: ", self.screen.screen_height)
            self.countChangeSizeLandscape += 1
            self.is_fullscreen = False

        self.ryo.update_landscape(self.landscape)


if __name__ == '__main__':
    ryo_carrot_game_object = RyoCarrotGame()
    ryo_carrot_game_object.run_ryo_carrot_game()
