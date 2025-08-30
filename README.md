# Alien Invasion Game

A Python-based 2D space shooter game built with Pygame, demonstrating Object-Oriented Programming concepts and clean code architecture.

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
- **Architecture**: Object-oriented design with modular class structure
- **Design Patterns**: Basic inheritance and encapsulation patterns
- **Code Quality**: Clean, readable code with proper documentation
- **Graphics**: 2D sprites and shapes
- **Sound**: Basic audio support (can be extended)

## 🎨 Customization

You can easily modify the game by editing the `settings.py` file:
- Change screen dimensions
- Adjust game speeds
- Modify colors and visual elements
- Tune difficulty parameters

## 💼 Portfolio Project

This project was created to demonstrate my learning journey in Python programming and Object-Oriented Programming concepts. It showcases:

### **Object-Oriented Programming**
- **Class Design**: Organized classes for game entities (Ship, Alien, Bullet)
- **Inheritance**: Implementation of inheritance for UI components
- **Encapsulation**: Separation of game logic into different modules
- **Modular Structure**: Clean organization of game systems

### **Learning Outcomes**
- **Python Fundamentals**: Classes, methods, and file organization
- **Game Development**: Basic game loop, event handling, and rendering
- **Code Organization**: Logical project structure and import management
- **Problem Solving**: Breaking down complex game mechanics into manageable parts

## 🌿 Branch Structure

This repository contains different versions and iterations of the game, demonstrating the development process:

### **`main`** (Default Branch)
- Complete, polished version with all features
- Full game loop, scoring system, and multiple levels
- Best demonstration of programming skills and game design
- Primary showcase version of the project

### **`basic`** (Basic Version)
- Initial version of the game with core mechanics
- Basic ship movement, alien spawning, and shooting
- Foundation for more advanced features

### **`sideways`** (Experimental Branch)
- Side projects and experimental features
- Testing new game mechanics and ideas
- Shows exploration of different programming approaches

### **`training`** (Learning Branch)
- Practice implementations and learning exercises
- Code experiments and skill development
- Demonstrates continuous learning and improvement

## 🤝 Contributing

This is a learning project, but I welcome feedback and suggestions:
- Report any bugs you find
- Suggest improvements or new features
- Share ideas for better code organization
- Help improve the documentation

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Inspired by classic arcade games
- Built as part of my Python learning journey
- Uses Pygame framework for game development
- Created to practice Object-Oriented Programming concepts

## 📞 Contact

For questions or feedback about this project, please open an issue on GitHub.

---

**Enjoy playing Alien Invasion!** 🚀👾 