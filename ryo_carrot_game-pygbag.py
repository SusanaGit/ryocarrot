import random
import sys
from datetime import time

import pygame
import asyncio

from ryo import Ryo
from screen import Screen
from settings import Settings
from carrot import Carrot
from babybunny import BabyBunny


class RyoCarrotGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
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

        self.font = pygame.font.SysFont(None, 48)

        self.create_images_counts()

        self.music()

    async def main(self):
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

            await asyncio.sleep(0)

    def choose_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.change_size_screen()
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.ryo.moving_right_ryo = True
                elif event.key == pygame.K_LEFT:
                    self.ryo.moving_left_ryo = True
                elif event.key == pygame.K_c or event.key == pygame.K_SPACE:
                    self.throw_carrots()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ryo.moving_right_ryo = False
                if event.key == pygame.K_LEFT:
                    self.ryo.moving_left_ryo = False

            elif event.type == pygame.FINGERDOWN:
                self.touch_start(event)
            elif event.type == pygame.FINGERUP:
                self.touch_end(event)
            elif event.type == pygame.FINGERMOTION:
                self.moving_ryo_mbile(event)

            elif event.type == self.CREATE_BABYBUNNY_EVENT:
                self.create_babybunnies()
                self.random_time_creation_babybunny()

    def update_landscape(self):
        self.landscape.blit(self.screen.background_image, (0, 0))
        self.ryo.draw_ryo_current_location()

        for carrot in self.carrots.sprites():
            carrot.draw_carrot()

        self.babybunnies.draw(self.landscape)

        self.show_happy_babybunnies()
        self.show_unhappy_babybunnies()

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
            print("happy baby bunnies:", self.babybunnies_happy_count)

    def delete_babybunny_disappeared(self):
        for babybunny in self.babybunnies.copy():
            if babybunny.rect.top >= self.landscape.get_height():
                self.babybunnies.remove(babybunny)
                self.babybunnies_unhappy_count += 1
                print("baby bunnies unhappy:", self.babybunnies_unhappy_count)

    def show_happy_babybunnies(self):
        rect_show_happy_babybunnies = pygame.Rect(self.screen.screen_width - 120, 10, 100, 100)
        self.landscape.blit(self.happy_babybunnies_image, rect_show_happy_babybunnies)

        happy_babybunnies_quantity_text = self.font.render(f"{self.babybunnies_happy_count}", True, (255, 165, 0))

        self.landscape.blit(happy_babybunnies_quantity_text, rect_show_happy_babybunnies)

    def show_unhappy_babybunnies(self):
        rect_show_unhappy_babybunnies = pygame.Rect(self.screen.screen_width - 120, 120, 100, 100)
        self.landscape.blit(self.unhappy_babybunnies_image, rect_show_unhappy_babybunnies)

        unhappy_babybunnies_quantity = self.font.render(f"{self.babybunnies_unhappy_count}", True, (255, 165, 0))
        self.landscape.blit(unhappy_babybunnies_quantity, rect_show_unhappy_babybunnies)

    def create_images_counts(self):
        self.happy_babybunnies_image = pygame.image.load("images/happy-baby-bunny.png")
        self.happy_babybunnies_image = pygame.transform.scale(self.happy_babybunnies_image, (100, 100))

        self.unhappy_babybunnies_image = pygame.image.load("images/unhappy-baby-bunny.png")
        self.unhappy_babybunnies_image = pygame.transform.scale(self.unhappy_babybunnies_image, (100, 100))

    def music(self):
        pygame.mixer.music.load("music/dreams.ogg")
        pygame.mixer.music.play(-1)
        print("Royalty Free Music: https://www.bensound.com License code: SES9TCRFZ5LYRORV")

    def touch_start(self, event):
        self.touch_start_position = (event.x * self.screen.screen_width, event.y * self.screen.screen_height)
        self.touch_start_position_y = self.touch_start_position[1]

    def touch_end(self, event):
        self.touch_end_y = event.y * self.screen.screen_height

    def moving_ryo_mbile(self, event):
        x = event.x * self.screen.screen_width
        y = event.y * self.screen.screen_height

        if self.touch_start_position_y is not None and y < self.touch_start_position_y - 50:
            self.throw_carrots()
            self.touch_start_position_y = None

        if x > self.touch_start_position[0]:
            self.ryo.moving_right_ryo = True
            self.ryo.moving_left_ryo = False
        elif x < self.touch_start_position[0]:
            self.ryo.moving_left_ryo = True
            self.ryo.moving_right_ryo = False
        else:
            self.ryo.moving_left_ryo = False
            self.ryo.moving_right_ryo = False

