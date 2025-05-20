"""
Pac-Man in Python | @TheWannabeCoder

The actors.py file is where we define the characters in our game.
This includes Pac-Man & the ghosts.
This is where we define our characters beavior.
"""

import turtle
import random
from constants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVE_SPEED, ENEMY_MOVE_SPEED, ENEMY_RADAR


class Actor(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def get_heading(self):
        return round(self.heading())

class Player(Actor):

    def __init__(self, walls):
        super().__init__()
        self.showturtle()
        self.shape("circle")
        self.shapesize(1.4)
        self.pencolor("white")
        self.fillcolor("yellow")
        self.state = "stop"
        self.move_speed = PLAYER_MOVE_SPEED
        self.lives = 3
        self.score = 0
        self.walls = walls

    def move(self):
        if self.state != "stop":
            self.forward(self.move_speed)
            # Screen wraparound:
            if round(self.ycor()) > SCREEN_HEIGHT / 2 - 2 * CELL_SIZE:
                self.sety(-SCREEN_HEIGHT / 2)
            elif round(self.ycor()) < -SCREEN_HEIGHT / 2:
                self.sety(SCREEN_HEIGHT / 2 - 2 * CELL_SIZE)
            elif round(self.xcor()) < -SCREEN_WIDTH / 2:
                self.setx(SCREEN_WIDTH / 2)
            elif round(self.xcor()) > SCREEN_WIDTH / 2:
                self.setx(-SCREEN_WIDTH / 2)


    def check_wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(CELL_SIZE / 2)
        # Loop through all the walls
        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            if heading == 0:  # Moving right
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - CELL_SIZE)
                    self.state = "stop"
                # Corrections
                elif -half_cell < dx + half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif -half_cell < dx + half_cell < half_cell and dy < -half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y - CELL_SIZE)

            elif heading == 180:  # Moving left
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + CELL_SIZE)
                    self.state = "stop"
                # Corrections
                elif -half_cell < dx - half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif -half_cell < dx - half_cell < half_cell and dy < -half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y - CELL_SIZE)

            elif heading == 90:  # Moving up
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)
                    self.state = "stop"
                # Corrections
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

            elif heading == 270:  # Moving down
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                    self.state = "stop"
                # Corrections
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

    def turn_right(self):
        self.setheading(0)
        self.state = "move"

    def turn_left(self):
        self.setheading(180)
        self.state = "move"

    def turn_up(self):
        self.setheading(90)
        self.state = "move"

    def turn_down(self):
        self.setheading(270)
        self.state = "move"

    def reset_speed(self):
        self.move_speed = PLAYER_MOVE_SPEED


class Enemy(Actor):

    def __init__(self, start_x, start_y, walls, player: Player):
        super().__init__()
        self.showturtle()
        self.shape("circle")
        self.shapesize(1.4)
        self.pencolor("white")
        self.fillcolor("red")
        self.goto(start_x, start_y)
        self.state = "stop"
        self.walls = walls
        self.player = player

    def move(self):
        if self.state != "stop":
            self.forward(ENEMY_MOVE_SPEED)
            # Screen wraparound:
            if round(self.ycor()) > SCREEN_HEIGHT / 2 - 2 * CELL_SIZE:
                self.sety(-SCREEN_HEIGHT / 2)
            elif round(self.ycor()) < -SCREEN_HEIGHT / 2:
                self.sety(SCREEN_HEIGHT / 2 - 2 * CELL_SIZE)
            elif round(self.xcor()) < -SCREEN_WIDTH / 2:
                self.setx(SCREEN_WIDTH / 2)
            elif round(self.xcor()) > SCREEN_WIDTH / 2:
                self.setx(-SCREEN_WIDTH / 2)
    
    def check_wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(CELL_SIZE / 2)
        # Loop through all the walls
        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            if heading == 0:  # Moving right
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - CELL_SIZE)
                    self.start_move()
                # Corrections
                elif -half_cell < dx + half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif -half_cell < dx + half_cell < half_cell and dy < -half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y - CELL_SIZE)

            elif heading == 180:  # Moving left
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + CELL_SIZE)
                    self.start_move()
                # Corrections
                elif -half_cell < dx - half_cell < half_cell and dy > half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y + CELL_SIZE)
                elif -half_cell < dx - half_cell < half_cell and dy < -half_cell and abs(dy) < CELL_SIZE:
                    self.sety(y - CELL_SIZE)

            elif heading == 90:  # Moving up
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - CELL_SIZE)
                    self.start_move()
                # Corrections
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy + half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

            elif heading == 270:  # Moving down
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + CELL_SIZE)
                    self.start_move()
                # Corrections
                elif dx > half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x + CELL_SIZE)
                elif dx < -half_cell and abs(dx) < CELL_SIZE and -half_cell < dy - half_cell < half_cell:
                    self.setx(x - CELL_SIZE)

    def start_move(self):
        # Calculate right, left, top and bottom cell aorund the enemy
        right_cell = round(self.xcor()) + CELL_SIZE, round(self.ycor())
        left_cell = round(self.xcor()) - CELL_SIZE, round(self.ycor())
        top_cell = round(self.xcor()), round(self.ycor()) + CELL_SIZE
        bottom_cell = round(self.xcor()), round(self.ycor()) - CELL_SIZE
        next_possibile_cell = [right_cell, left_cell, top_cell, bottom_cell]
        # Loop through all possible directions
        for cell in next_possibile_cell[:]:
            # Ensure it is not a wall
            if cell in self.walls:
                next_possibile_cell.remove(cell)
        next_cell = random.choice(next_possibile_cell)
        if next_cell == right_cell:
            self.setheading(0)
        elif next_cell == left_cell:
            self.setheading(180)
        elif next_cell == top_cell:
            self.setheading(90)
        elif next_cell == bottom_cell:
            self.setheading(270)
        self.state = "move"


    def go_after_player(self):
        player_x = round(self.player.xcor())
        player_y = round(self.player.ycor())
        enemy_x = round(self.xcor())
        enemy_y = round(self.ycor())
        # Moving left or right
        if ((self.get_heading() == 0 or self.get_heading() == 180) and
                self.distance(self.player) <= ENEMY_RADAR):
            if (player_y > enemy_y and
                    player_x + CELL_SIZE / 2 > enemy_x > player_x - CELL_SIZE / 2):
                self.setheading(90)
            elif (player_y < enemy_y and
                  player_x + CELL_SIZE / 2 > enemy_x > player_x - CELL_SIZE / 2):
                self.setheading(270)
        # Moving up or down
        elif ((self.get_heading() == 90 or self.get_heading() == 270) and
                self.distance(self.player) <= ENEMY_RADAR):
            if (player_y + CELL_SIZE / 2 > enemy_y > player_y - CELL_SIZE / 2 and
                    player_x > enemy_x):
                self.setheading(0)
            elif (player_y + CELL_SIZE / 2 > enemy_y > player_y - CELL_SIZE / 2 and
                  player_x < enemy_x):
                self.setheading(180)
        # Moving on same row or column as Pac-Man
        if player_y == enemy_y and player_x > enemy_x and self.distance(self.player) < ENEMY_RADAR:
            self.setheading(0)
        elif player_y == enemy_y and player_x < enemy_x and self.distance(self.player) < ENEMY_RADAR:
            self.setheading(180)
        elif player_x == enemy_x and player_y > enemy_y and self.distance(self.player) < ENEMY_RADAR:
            self.setheading(90)
        elif player_x == enemy_x and player_y < enemy_y and self.distance(self.player) < ENEMY_RADAR:
            self.setheading(270)


