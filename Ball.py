from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("yellow")
        self.penup()
        self.x = 3
        self.y = 3
        self.move_speed = 0.001

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def x_bounce(self):
        self.x *= -1

    def y_bounce(self):
        self.y *= -1
