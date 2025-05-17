"""
Pac-Man in Python | @TheWannabeCoder

The actors.py file is where we define the characters in our game.
This includes Pac-Man & the ghosts.
This is where we define our characters beavior.
"""

import turtle
from constants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVE_SPEED


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
            # Screen wraparound
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
