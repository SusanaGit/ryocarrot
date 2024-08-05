import pygame

from screen import Screen


class RyoCarrotGame:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.landscape = None

        self.initialize_screen()

        self.countChangeSizeLandscape = 0

    def run_ryo_carrot_game(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.change_size_screen()

            self.landscape.fill(self.screen.bg_color)
            pygame.display.flip()

        pygame.quit()

    def initialize_screen(self):
        self.screen = Screen()
        self.landscape = pygame.display.set_mode(
            (self.screen.screen_width,
             self.screen.screen_height)
        )
        pygame.display.set_caption(self.screen.app_title)


    def change_size_screen(self):
        if self.countChangeSizeLandscape % 2 == 0:
            self.landscape = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.countChangeSizeLandscape += 1
        else:
            self.landscape = pygame.display.set_mode((self.screen.screen_width, self.screen.screen_height))
            self.countChangeSizeLandscape += 1

if __name__ == '__main__':
    ryo_carrot_game_object = RyoCarrotGame()
    ryo_carrot_game_object.run_ryo_carrot_game()
