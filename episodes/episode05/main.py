"""
Pac-Man in Python | @TheWannabeCoder

The main.py file is the starting point of the game.
It's where everything gets set up and launched
"""

import turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from renderer import Wall, Pellet, PowerPellet
from actors import Player


def init_screen():
    "Game main screen setup"
    # Create main game screen
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Episode 3: Pac-Man in Python - Layout #2 | @TheWannabeCoder")
    screen.setup(SCREEN_WIDTH + 10, SCREEN_HEIGHT + 10)
    screen.bgcolor("black")
    return screen


def bind_controls(screen, player):
    "Keyboard & mouse bindings"
    # Tell the screen to be aware for keyboard or mouse clicks
    screen.listen()
    # Bind controls
    screen.onkeypress(player.turn_right, "Right")
    screen.onkeypress(player.turn_left, "Left")
    screen.onkeypress(player.turn_up, "Up")
    screen.onkeypress(player.turn_down, "Down")


def game_loop(screen, player):
    "Real time updates"
    # Update player
    player.move()
    player.check_wall_collision()
    # Update screen
    screen.update()
    # Repeat the function every 16ms
    screen.ontimer(lambda: game_loop(
        screen, player), 1000 // 60)


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
    walls = wall_pen.walls
    pellet_pen.draw()
    power_pen.draw()
    # Player starting position
    player_start_coor = random.choice(pellet_pen.pellets)
    player_start_x = player_start_coor[0]
    player_start_y = player_start_coor[1]
    # Create Pac-Man
    player = Player(walls)
    player.goto(player_start_x, player_start_y)
    # Bind controls
    bind_controls(screen, player)
    # Enable real-time updates
    game_loop(screen, player)
    # Keeps the main screen open
    screen.mainloop()

# Ensures the game starts only when main.py is run directly, not imported
if __name__ == "__main__":
    main()
