class GameStats:
    """Track statistics for Alien Invation."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0
        self._load_high_score()  # Load the high score from file when the game starts

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _save_high_score(self):
        """Save high score to file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def _load_high_score(self):
         """Load high score from file."""
         try:
             with open("high_score.txt", "r") as file:
                 self.high_score = int(file.read())
         except FileNotFoundError:
             self.high_score = 0
