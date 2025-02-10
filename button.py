import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.heigh = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.heigh)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

        # Create instruction text and properties
        self.instruction_font = pygame.font.SysFont(None, 25)
        self.instruction_text_color = (0, 135, 0)
        self._prep_instruction("Press 'P' to start the game")

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _prep_instruction (self, text):
        """Render the instruction text below the button."""
        self.instruction_image = self.instruction_font.render(text, True, self.instruction_text_color)
        self.instruction_rect = self.instruction_image.get_rect()
        self.instruction_rect.centerx = self.rect.centerx
        self.instruction_rect.top = self.rect.bottom + 10  # Position below button

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.instruction_image, self.instruction_rect)