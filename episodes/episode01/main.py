"""
Pac-Man in Python | @TheWannabeCoder

The main.py file is the starting point of the game.
It's where everything gets set up and launched
"""

import turtle

def init_screen():
    "Initialize main screen, and returns it when called"
    # Create the game screen and store it in a variable screen
    screen = turtle.Screen()
    # Disable auto screen update
    screen.tracer(0)
    # Set screen title
    screen.title("Episode 1: Pac-Man in Python - Setup | @TheWannabeCoder")
    # Set screen size
    screen.setup(1000, 800)
    # Set screen background color
    screen.bgcolor("black")
    # Return the game screen when function is called
    return screen


def game_loop(screen):
    """
    This is the game engine.
    Keeps everything moving, updating and reacting in real time.
    """
    # Update screen
    screen.update()


def main():
    """
    This function starts the game, it sets everything up - the screen, the players and levels.
    After setting up, it kicks off the game loop where things move and interact.
    """
    # Call the screen initiation function
    screen = init_screen()
    # Game loop - moving things
    game_loop(screen)
    # Keeps the main screen open
    screen.mainloop()


# This makes sure the game only starts when we run this file directly-
# not if it's being imported as a module in another file.
if __name__ == "__main__":
    main()
