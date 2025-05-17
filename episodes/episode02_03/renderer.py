"""
Pac-Man in Python | @TheWannabeCoder

The renderer.py file is where all the drawing of static objects happens.
We use Turtle Graphics to create pens that draw walls, pellets, power pellets -
using the coordinates from our maze layout, and to draw the user interface on screen.
"""

import turtle
from mazes import calculate_maze_data, maze_level_1


class Pen(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
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
        # walls is a list of tuples, each tuple contains the x, y coordinates of a wall center
        # Iterate over each wall coordinate inside the walls list
        for x, y in self.walls:
            self.goto(x, y)
            # stamp the wall
            self.stamp()


class Pellet(Pen):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.35, 0.35)
        self.pencolor("white")
        self.fillcolor("gold")

    def draw(self):
        "Draw the pellet on screen"
        for x, y in self.pellets:
            self.goto(x, y)
            # stamp the pellet
            self.stamp()


class PowerPellet(Pen):
    "Pallet for Pac-Man to eat"

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.pencolor("white")
        self.fillcolor("chartreuse")

    def draw(self):
        "Draw the pellet on screen"
        for x, y in self.power_pellets:
            self.goto(x, y)
            # stamp the power pellet
            self.stamp()
