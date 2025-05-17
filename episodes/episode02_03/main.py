"""
Pac-Man in Python | @TheWannabeCoder

The main.py file is the starting point of the game.
It's where everything gets set up and launched
"""

import turtle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from renderer import Wall, Pellet, PowerPellet


def init_screen():
    "Game main screen setup"
    # Create main game screen
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Episode 3: Pac-Man in Python - Layout #2 | @TheWannabeCoder")
    screen.setup(SCREEN_WIDTH + 10, SCREEN_HEIGHT + 10)
    screen.bgcolor("black")
    return screen


def game_loop(screen):
    "Real time updates"
    # Update screen
    screen.update()


def main():
    "Main function - setting up the game"
    # Creating the screen
    screen = init_screen()
   # Create rendering instances
    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pen = PowerPellet()
    # Call the instance functions
    wall_pen.draw()
    pellet_pen.draw()
    power_pen.draw()
    # Enable real-time updates
    game_loop(screen)
    # Keeps the main screen open
    screen.mainloop()

# Ensures the game starts only when main.py is run directly, not imported
if __name__ == "__main__":
    main()
