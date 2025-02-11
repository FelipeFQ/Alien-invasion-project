class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230 ,230) 
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullets settings
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Square settings
        self.square_width = 70
        self.square_height = 70  
        self.square_speed = 1.0
        self.square_color = (255, 0, 0)  
        self.misses_limit = 10
        self.hits = 0

        # Square_direction 
        self.x_square_direction = 1
        self.y_square_direction = 1