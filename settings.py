class Settings:

    def __init__(self):
        self.initialize_ryo_speeds()

    def initialize_ryo_speeds(self):
        self.ryo_speed_small = 2
        self.ryo_speed_fullscreen = 10

    def initialize_carrots(self):
        self.carrot_speed = 1
        self.carrot_width = 3
        self.carrot_height = 15
        self.carrot_color = (60,60,60)