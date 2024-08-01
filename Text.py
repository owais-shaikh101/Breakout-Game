from turtle import Turtle


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.lives = 3
        self.goto(x=-575, y=220)
        self.write(f"Score: {self.score}\nLives: {self.lives}", False, align="Left", font=("Arial", 20, "normal"))
