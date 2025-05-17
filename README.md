# Pac-Man in Python 🐍🎮

This is a beginner-friendly Pac-Man clone built using Python's Turtle Graphics module.

The code is part of a full YouTube tutorial series, where we build the game step by step — covering everything from drawing the maze to player movement, collision logic, and more.

## 🎥 Watch the Tutorial Series

YouTube Playlist: [Pac-Man in Python - Full Tutorial Series](https://www.youtube.com/playlist?list=PL1XCNNzXQuPPglJxBB2itjcnX3U8g3U0q)

Follow along to:
- Learn basic game development concepts
- Use Python's Turtle module for graphics
- Practice clean, modular code structure
- Build a playable Pac-Man game from scratch

## 📁 Project Structure

```
pacman-turtle-python/
│
├── README.md
├── LICENSE
├── .gitignore
│
└── episodes/
    ├── episode01_setup/
    │   └── main.py
    │
    ├── episode02_03_grid_and_maze/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode04_player_movement/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   ├── renderer.py
    │   └── actors.py
    │
    ├── episode05_wall_collision/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   ├── renderer.py
    │   └── actors.py
    │
    ├── episode06_pellets_ui/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   ├── renderer.py
    │   └── actors.py
    │
    ├── episode07_enemies_basic/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   ├── renderer.py
    │   └── actors.py
    │
    ├── episode08_enemy_ai_polish/
    │   ├── main.py
    │   ├── constants.py
    │   ├── mazes.py
    │   ├── renderer.py
    │   └── actors.py
    │
    └── episode09_shapes_and_sounds/   # Final game + assets
        ├── main.py
        ├── constants.py
        ├── mazes.py
        ├── renderer.py
        ├── actors.py
        ├── pac.gif
        ├── up.gif
        ├── down.gif
        ├── left.gif
        ├── right.gif
        ├── wall.gif
        ├── red_enemy.gif
        ├── blue_enemy.gif
        ├── pink_enemy.gif
        ├── green_enemy.gif
        ├── start_up.wav
        ├── eat.wav
        └── death.wav

```

📦 **Note:**  
`episode09_shapes_and_sounds/` contains the **final version** of the game, including all custom graphics and sound effects.  
If you just want to play the complete Pac-Man clone, you can jump straight to that folder.

## 🐍 Requirements

No external libraries needed – just Python 3.x.

Make sure `turtle` is available (it's included with standard Python installs).

## ▶️ How to Run

```bash
python main.py
```

The game window will open, and you can start playing Pac-Man using the arrow keys!

## 📌 About the Creator

Created by TheWannabeCoder  
Making simple, hands-on Python tutorials for beginners.  
YouTube: [@TheWannabeCoder](https://www.youtube.com/@TheWannabeCoder)

## 📜 License

This project is licensed under the MIT License.
