class Settings():
    """A class to store all Game Settings"""


    def __init__(self):
        """Screen Settings"""
        #background color
        self.bg_color = (0, 0, 0)
        #resolution
        self.screen_height=1200
        self.screen_width=1500

        #ships speed
        self.ship_speed_factor =3
        self.ship_lives=3

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 30
        self.bullet_height =7
        self.bullet_color=(250,0,0)

        #alien speed
        self.fleet_drop_factor = 500
        self.speedup_scale=1.1
        self.initzialize_dynamic_settings()

    def initzialize_dynamic_settings(self):
        """inits the settings that change per level"""
        self.ship_speed=1.5
        self.bullet_speed=3
        self.alien_speed = 1
        # fleet direction of 1, alien move to the right: 1 =right;-1=left
        self.alien_direction=1

    def increase_speed(self):
        """increases speed"""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_Speed_factor *=self.speedup_scale

