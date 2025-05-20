# Pac-Man in Python 🐍🎮

This is a beginner-friendly Pac-Man clone built using Python's Turtle Graphics module.

The code is part of a full YouTube tutorial series, where we build the game step by step — covering everything from drawing the maze to player movement, collision logic, and more.

## 🎥 Watch the Tutorial Series

YouTube Playlist: [Pac-Man in Python - Full Tutorial Series](https://www.youtube.com/playlist?list=PL1XCNNzXQuPPglJxBB2itjcnX3U8g3U0q)

---

## 📚 Table of Contents

Use the links below to access the code for each episode:

1. [Episode 1 – Project & Screen Setup](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode01)
2. [Episodes 2 & 3 – Grid & Maze Drawing](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode02_03)
3. [Episode 4 – Player Setup](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode04)
4. [Episode 5 – Wall Collision](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode05)
5. [Episode 6 – UI & Pellet Collection](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode06)
6. [Episode 7 – Enemies Setup](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode07)
7. [Episode 8 – Enemy AI & Final Polish](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode08)
8. [Episode 9 – Final Game: Shapes & Sounds](https://github.com/TheWannabeCoder92/pacman-turtle-python/tree/main/episodes/episode09)

📂 [View Full Project Structure](#-project-structure)

---

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
    ├── episode01/       # Project & Screen setup
    |   ├── README.md
    │   └── main.py
    │
    ├── episode02_03/    # Grid & Maze Drawing
    |   ├── README.md
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode04/       # Player setup
    |   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode05/       # Wall Collision
    |   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode06/       # UI & Pellet Collection
    |   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode07/       # Enemies Setup
    |   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    ├── episode08/       # Enemy AI & Final Polish
    |   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── mazes.py
    │   └── renderer.py
    │
    └── episode09/       # Final Game: Shapes & Sounds
        ├── README.md
        ├── actors.py
        ├── constants.py
        ├── death.wav
        ├── down.gif
        ├── eat.wav
        ├── green_enemy.gif
        ├── left.gif
        ├── main.py
        ├── mazes.py
        ├── pac.gif
        ├── pink_enemy.gif
        ├── red_enemy.gif
        ├── renderer.py
        ├── right.gif
        ├── start_up.wav
        ├── up.gif
        └── wall.gif
```

📦 **Note:**  
`episode09/` contains the **final version** of the game, including all custom graphics and sound effects.  
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
