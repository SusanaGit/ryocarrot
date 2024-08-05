import pygame

from screen import Screen


class RyoCarrotGame:
    def __init__(self):
        pygame.init()

        self.screen = None
        self.landscape = None

        self.initialize_screen()

    def run_ryo_carrot_game(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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


if __name__ == '__main__':
    ryo_carrot_game_object = RyoCarrotGame()
    ryo_carrot_game_object.run_ryo_carrot_game()
