# Alien Invasion Game

A Python-based 2D space shooter game built with Pygame, inspired by classic arcade games.

## 🎮 Game Description

Alien Invasion is a space shooter game where you control a spaceship and defend Earth from invading aliens. The game features multiple levels, increasing difficulty, scoring system, and smooth gameplay mechanics.

## ✨ Features

- **Ship Movement**: Control your spaceship with arrow keys or WASD
- **Alien Fleet**: Multiple rows of aliens that move in formation
- **Shooting Mechanics**: Fire bullets to destroy aliens
- **Progressive Difficulty**: Game gets harder as you advance through levels
- **Scoring System**: Track your score and compete for high scores
- **Level System**: Multiple difficulty levels with increasing challenge
- **Game States**: Menu system with Play button and game over handling
- **Visual Effects**: Smooth animations and responsive controls

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/FelipeFQ/Alien-invasion-project.git
   cd Alien-invasion-project
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python alien_invasion.py
   ```

## 🎯 How to Play

### Controls
- **Arrow Keys** or **WASD**: Move the spaceship left/right
- **Spacebar**: Fire bullets
- **P**: Pause game
- **Q**: Quit game
- **Mouse**: Navigate menus

### Gameplay
1. Start the game and click the "Play" button
2. Control your spaceship to avoid alien attacks
3. Shoot down aliens to earn points
4. Survive as long as possible and achieve high scores
5. Game ends when aliens reach the bottom or hit your ship

### Scoring
- Different aliens have different point values
- Score increases with each level
- Try to beat your highest score!

## 📁 Project Structure

```
Alien invasion project/
├── alien_invasion.py      # Main game file
├── alien.py               # Alien class and behavior
├── bullet.py              # Bullet class and mechanics
├── button.py              # Button UI components
├── game_stats.py          # Game statistics and state
├── scoreboard.py          # Score display and tracking
├── settings.py            # Game configuration
├── ship.py                # Player ship class
├── images/                # Game assets
│   ├── alien.bmp         # Alien sprite
│   └── ship.bmp          # Ship sprite
└── README.md              # This file
```

## 🛠️ Technical Details

- **Framework**: Pygame
- **Language**: Python 3
- **Architecture**: Object-oriented design with separate classes for game entities
- **Graphics**: 2D sprites and shapes
- **Sound**: Basic audio support (can be extended)

## 🎨 Customization

You can easily modify the game by editing the `settings.py` file:
- Change screen dimensions
- Adjust game speeds
- Modify colors and visual elements
- Tune difficulty parameters

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Inspired by classic arcade games
- Built as part of Python learning journey
- Uses Pygame framework for game development

## 📞 Contact

For questions or feedback about this project, please open an issue on GitHub.

---

**Enjoy playing Alien Invasion!** 🚀👾 