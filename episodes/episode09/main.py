"""
Pac-Man in Python | @TheWannabeCoder

The main.py file is the starting point of the game.
It's where everything gets set up and launched
"""

import turtle
import random
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, ENEMY_NUMBER
from renderer import Wall, Pellet, PowerPellet, UiPen
from actors import Player, Enemy


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


def game_loop(screen, player, score_pen, lives_pen, pellet_pen, power_pen, player_start_x, player_start_y, enemies):
    "Real time updates"
    # Update score, lives and game messages
    score_pen.write_score(player.score, player.lives, pellet_pen.stamps, power_pen.stamps)
    lives_pen.write_lives(player.lives, pellet_pen.stamps, power_pen.stamps)
    # Collision: player-pellet
    for (px, py), stamp_id in list(pellet_pen.stamps.items()):
        if player.distance(px, py) < CELL_SIZE / 2 and (px, py) != (player_start_x, player_start_y):
            os.system("aplay eat.wav&")
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
            os.system("aplay eat.wav&")
            power_pen.clearstamp(stamp_id)
            del power_pen.stamps[(px, py)]
            player.score += 50
            # Speed boost
            player.move_speed += 3
            screen.ontimer(player.reset_speed, 3000)
    # Update Player
    player.move()
    player.check_wall_collision()
    # Update Enemies
    for enemy in enemies:
        enemy.move()
        enemy.check_wall_collision()
        enemy.go_after_player()
        # Collision: player-enemy
        if enemy.distance(player) < CELL_SIZE / 2:
            os.system("aplay death.wav&")
            # Ensure player does not spawn near enemy
            safe_spots = []
            for pellet in pellet_pen.pellets:
                if all(enemy.distance(pellet) > CELL_SIZE * 5 for enemy in enemies):
                    safe_spots.append(pellet)
            player.goto(random.choice(safe_spots))
            player.lives -= 1        
    # Win game - stop everything and close the game
    if len(power_pen.stamps) == 0 and len(pellet_pen.stamps) == 0:
        player.state = "stop"
        for enemy in enemies:
            enemy.hideturtle()
            enemy.state = "stop"
        screen.ontimer(lambda: screen.bye(), 3000)
    # Game over - stop everything and close the game
    if player.lives == 0:
        player.state = "stop"
        player.hideturtle()
        for enemy in enemies:
            enemy.state = "stop"
        screen.ontimer(lambda: screen.bye(), 3000)
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
            player_start_y,
            enemies
        ),
        1000 // 60
    )


def main():
    "Main function - setting up the game"
    # Create the screen & register shapes
    screen = init_screen()
    screen.register_shape("pac.gif")
    screen.register_shape("up.gif")
    screen.register_shape("down.gif")
    screen.register_shape("left.gif")
    screen.register_shape("right.gif")
    screen.register_shape("green_enemy.gif")
    screen.register_shape("pink_enemy.gif")
    screen.register_shape("red_enemy.gif")
    screen.register_shape("wall.gif")
   # Create rendering instances
    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pen = PowerPellet()
    ui_pen = UiPen()
    score_pen = UiPen()
    lives_pen = UiPen()
    # Call the instance methods and get attributes
    wall_pen.draw()
    walls = wall_pen.walls
    pellet_pen.draw()
    pellets = pellet_pen.pellets
    power_pen.draw()
    ui_pen.draw_ui_area()
    # Player starting position
    player_start_coor = random.choice(pellet_pen.pellets)
    player_start_x = player_start_coor[0]
    player_start_y = player_start_coor[1]
    # Create Pac-Man
    player = Player(walls)
    player.goto(player_start_x, player_start_y)
    # Create enemies
    enemy_colors = ["green_enemy.gif", "pink_enemy.gif", "red_enemy.gif"]
    enemies = []
    for _ in range(ENEMY_NUMBER):
        # Ensure enemy does not spawn near player
        safe_spots = []
        for pellet in pellets:
            if player.distance(pellet) > CELL_SIZE * 5:
                 safe_spots.append(pellet)
        enemy_start_x, enemy_start_y = random.choice(safe_spots)
        enemy = Enemy(enemy_start_x, enemy_start_y, walls, player)
        enemy.shape(random.choice(enemy_colors))
        enemies.append(enemy)
    # Start of the game settings
    os.system("aplay start_up.wav&")
    screen.ontimer(lambda: bind_controls(screen, player), 2500)
    for enemy in enemies:
        screen.ontimer(enemy.start_move, 2500)
    # Enable real-time updates
    game_loop(screen, player, score_pen, lives_pen, pellet_pen,
              power_pen, player_start_x, player_start_y, enemies)
    # Keeps the main screen open
    screen.mainloop()

# Ensures the game starts only when main.py is run directly, not imported
if __name__ == "__main__":
    main()
