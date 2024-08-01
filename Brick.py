from turtle import Turtle
import random


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.x = -520
        self.y = 190
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        for i in range(50):
            r = random.randrange(50, 255)
            g = random.randrange(50, 255)
            b = random.randrange(50, 255)
            brick = Turtle()
            brick.penup()
            brick.shape("square")
            brick.color((r, g, b))
            brick.shapesize(1.5, 5.5)
            brick.goto(x=self.x, y=self.y)
            self.x += 115
            if i == 9:
                self.y -= 35
                self.x = -520
            elif i == 19:
                self.y -= 35
                self.x = -520
            elif i == 29:
                self.y -= 35
                self.x = -520
            elif i == 39:
                self.y -= 35
                self.x = -520
            elif i == 49:
                self.y -= 35
                self.x = -520
            self.bricks.append(brick)