"""
Pac-Man in Python | @TheWannabeCoder

The renderer.py file is where all the drawing of static objects happens.
We use Turtle Graphics to create pens that draw walls, pellets, power pellets -
using the coordinates from our maze layout, and to draw the user interface on screen.
"""

import turtle
from mazes import calculate_maze_data, maze_level_1
from constants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


class Pen(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("silver")
        self.speed(0)
        # Get all coordinates from the maze level
        self.walls, self.pellets, self.power_pellets = calculate_maze_data(
            maze_level_1)



class Wall(Pen):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1.2)
        self.pencolor("white")
        self.fillcolor("dodger blue")

    def draw(self):
        "Draw the wall on screen"
        for x, y in self.walls:
            self.goto(x, y)
            self.stamp()


class Pellet(Pen):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.35, 0.35)
        self.pencolor("white")
        self.fillcolor("gold")
        self.stamps = {}

    def draw(self):
        "Draw the pellet on screen"
        for x, y in self.pellets:
            self.goto(x, y)
            # stamp the pellet and save the stamp id of the coordinate in a variable
            stamp_id = self.stamp()
            # Add the coordinate to the dictionary and map it to the saved stamp_id
            self.stamps[(x, y)] = stamp_id


class PowerPellet(Pen):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.pencolor("white")
        self.fillcolor("chartreuse")
        self.stamps = {}

    def draw(self):
        "Draw the pellet on screen"
        for x, y in self.power_pellets:
            self.goto(x, y)
            # stamp the power pellet and save the stamp id of the coordinate in a variable
            stamp_id = self.stamp()
            # Add the coordinate to the dictionary and map it to the saved stamp_id
            self.stamps[(x, y)] = stamp_id


class UiPen(Pen):

    def __init__(self):
        super().__init__()
        self.font = ("Courier", 30, "normal")

    def draw_ui_area(self):
        "UI Drawinddg"
        self.pensize(2)
        x = 0.9 * SCREEN_WIDTH / 2
        top_y = 0.98 * SCREEN_HEIGHT / 2
        bottom_y = top_y - 1.5 * CELL_SIZE
        self.goto(x, top_y)
        self.pendown()
        self.goto(-x, top_y)
        self.goto(-x, bottom_y)
        self.goto(x, bottom_y)
        self.goto(x, top_y)

    def write_score(self, score):
        "Write score on screen"
        self.clear()
        msg = f"Score: {score}"
        self.goto(-0.7 * SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 2 * CELL_SIZE)
        self.write(msg, False, "left", self.font)

    def write_lives(self, lives):
        "Write lives on screen"
        self.clear()
        msg = f"Lives: {lives}"
        self.goto(0.7 * SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 2 * CELL_SIZE)
        self.write(msg, False, "right", self.font)
