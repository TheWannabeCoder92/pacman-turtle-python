"""
Pac-Man in Python | @TheWannabeCoder

The main.py file is the starting point of the game.
It's where everything gets set up and launched
"""

import turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
from renderer import Wall, Pellet, PowerPellet, UiPen
from actors import Player


def init_screen():
    "Game main screen setup"
    # Create main game screen
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Pac-Man in Python | @TheWannabeCoder")
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


def game_loop(screen, player, score_pen, lives_pen, pellet_pen, power_pen, player_start_x, player_start_y):
    "Real time updates"
    # Update score, lives and game messages
    score_pen.write_score(player.score)
    lives_pen.write_lives(player.lives)
    # Collision: player-pellet
    for (px, py), stamp_id in list(pellet_pen.stamps.items()):
        if player.distance(px, py) < CELL_SIZE / 2 and (px, py) != (player_start_x, player_start_y):
            pellet_pen.clearstamp(stamp_id)
            del pellet_pen.stamps[(px, py)]
            player.score += 2
        # Skip points on game start from first pellet
        elif player.distance(px, py) < CELL_SIZE / 2 and (px, py) == (player_start_x, player_start_y):
            pellet_pen.clearstamp(stamp_id)
            del pellet_pen.stamps[(px, py)]
    # Collision: player-power pellet
    for (px, py), stamp_id in list(power_pen.stamps.items()):
        if player.distance(px, py) < CELL_SIZE / 2:
            power_pen.clearstamp(stamp_id)
            del power_pen.stamps[(px, py)]
            player.score += 50
            # Speed boost
            player.move_speed += 3
            screen.ontimer(player.reset_speed, 3000)
    # Update player
    player.move()
    player.check_wall_collision()
    # Update screen
    screen.update()
    # Repeat the function every 16ms
    screen.ontimer(
        lambda: game_loop(
            screen,
            player,
            score_pen,
            lives_pen,
            pellet_pen,
            power_pen,
            player_start_x,
            player_start_y
        ),
        1000 // 60
    )


def main():
    "Main function - setting up the game"
    # Creating the screen
    screen = init_screen()
   # Create rendering instances
    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pen = PowerPellet()
    ui_pen = UiPen()
    score_pen = UiPen()
    lives_pen = UiPen()
    # Call the instance functions
    wall_pen.draw()
    walls = wall_pen.walls
    pellet_pen.draw()
    power_pen.draw()
    ui_pen.draw_ui_area()
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
    game_loop(screen, player, score_pen, lives_pen, pellet_pen,
              power_pen, player_start_x, player_start_y)
    # Keeps the main screen open
    screen.mainloop()

# Ensures the game starts only when main.py is run directly, not imported
if __name__ == "__main__":
    main()
