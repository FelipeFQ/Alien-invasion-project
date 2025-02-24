import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg, x_offset=0, width=200, height=50, color=(253, 255, 73), text_size=48, instruction_text=None):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = (3, 2, 0)
        self.font = pygame.font.SysFont(None, text_size)

        # Build the button's rect object and posotion it with X_offset.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.x += x_offset 

        # The button message needs to be prepped only once.
        self._prep_msg(msg)
        self.msg = msg

        self.instruction_text = instruction_text
        if self.instruction_text:
            self._prep_instruction(self.instruction_text)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _prep_instruction (self, text):
        """Render the instruction text below the button."""
        if text:
            self.instruction_font = pygame.font.SysFont(None, 25)
            self.instruction_text_color = self.button_color
            self.instruction_image = self.instruction_font.render(text, True, self.instruction_text_color)
            self.instruction_rect = self.instruction_image.get_rect()
            self.instruction_rect.centerx = self.rect.centerx
            self.instruction_rect.top = self.rect.top - 20  # Position above button

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        if self.instruction_text:
            self.screen.blit(self.instruction_image, self.instruction_rect)