import random
import sys
import pygame

from ryo import Ryo
from screen import Screen
from settings import Settings
from carrot import Carrot
from babybunny import BabyBunny


class RyoCarrotGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = Screen()
        self.landscape = None
        self.is_fullscreen = False
        self.countChangeSizeLandscape = 0

        self.initialize_screen()
        self.ryo = Ryo(self)

        self.carrots = pygame.sprite.Group()
        self.babybunnies = pygame.sprite.Group()

        self.event_babybunny_creation_time_random()

        self.babybunnies_happy_count = 0
        self.babybunnies_unhappy_count = 0

    def run_ryo_carrot_game(self):
        running = True

        while running:
            self.choose_events()

            self.ryo.update_position_ryo(self.is_fullscreen)

            self.carrots.update()

            self.delete_carrots_disappeared()

            self.babybunnies.update()

            self.delete_babybunny_disappeared()

            self.eating_babybunny()

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
                elif event.key == pygame.K_c:
                    self.throw_carrots()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ryo.moving_right_ryo = False
                if event.key == pygame.K_LEFT:
                    self.ryo.moving_left_ryo = False

            elif event.type == self.CREATE_BABYBUNNY_EVENT:
                self.create_babybunnies()
                self.random_time_creation_babybunny()

    def update_landscape(self):
        self.landscape.blit(self.screen.background_image, (0, 0))
        self.ryo.draw_ryo_current_location()

        for carrot in self.carrots.sprites():
            carrot.draw_carrot()

        self.babybunnies.draw(self.landscape)

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
            self.countChangeSizeLandscape += 1
            self.is_fullscreen = True
        else:
            self.screen.initialize_screen()
            self.landscape = pygame.display.set_mode(
                (self.screen.screen_width,
                 self.screen.screen_height)
            )
            self.countChangeSizeLandscape += 1
            self.is_fullscreen = False

        self.ryo.update_landscape(self.landscape)

    def throw_carrots(self):
        new_carrot = Carrot(self)
        self.carrots.add(new_carrot)

    def delete_carrots_disappeared(self):
        for carrot in self.carrots.copy():
            if carrot.rect.bottom <= 0:
                self.carrots.remove(carrot)

    def create_babybunnies(self):
        new_babybunny = BabyBunny(self)
        self.babybunnies.add(new_babybunny)

    def random_time_creation_babybunny(self):
        random_time_creation_babybunny = random.randint(3000, 5000)
        pygame.time.set_timer(self.CREATE_BABYBUNNY_EVENT, random_time_creation_babybunny)

    def event_babybunny_creation_time_random(self):
        self.CREATE_BABYBUNNY_EVENT = pygame.USEREVENT + 1
        self.random_time_creation_babybunny()

    def eating_babybunny(self):
        babybunny_happy = pygame.sprite.groupcollide(
            self.babybunnies, self.carrots, True, True)

        if babybunny_happy:
            self.babybunnies_happy_count += 1
            print("baby bunnies happy:", self.babybunnies_happy_count)

    def delete_babybunny_disappeared(self):
        for babybunny in self.babybunnies.copy():
            if babybunny.rect.top >= self.landscape.get_height():
                self.babybunnies.remove(babybunny)
                self.babybunnies_unhappy_count += 1
                print("baby bunnies unhappy:", self.babybunnies_unhappy_count)


if __name__ == '__main__':
    ryo_carrot_game_object = RyoCarrotGame()
    ryo_carrot_game_object.run_ryo_carrot_game()
