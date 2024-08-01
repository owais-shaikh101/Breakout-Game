from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape('square')
        self.shapesize(1, 7)
        self.penup()
        self.color("green")
        self.goto(x=0, y=-275)

    def move_right(self):
        new_xpos = self.xcor() + 40
        if new_xpos < 516:
            self.goto(x=new_xpos, y=self.ycor())
        else:
            new_xpos = 516
            self.setx(new_xpos)

    def move_left(self):
        new_xpos = self.xcor() - 40
        if self.xcor() > -523:
            self.goto(x=new_xpos, y=self.ycor())
        else:
            new_xpos = -523
            self.setx(new_xpos)

