class Settings:

    def __init__(self):
        self.initialize_ryo_speeds()
        self.initialize_carrots_speeds()
        self.initialize_babybunny()

    def initialize_ryo_speeds(self):
        self.ryo_speed_small = 2
        self.ryo_speed_fullscreen = 10

    def initialize_carrots_speeds(self):
        self.carrot_speed = 2
        self.carrot_width = 30
        self.carrot_height = 30

    def initialize_babybunny(self):
        self.babybunny_speed = 2
        self.babybunny_width = 100
        self.babybunny_height = 100