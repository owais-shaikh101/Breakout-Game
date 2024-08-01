import time
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Brick import Brick
from Text import Text

screen = Screen()
screen.title("The Breakout Game")
screen.bgcolor("black")
screen.setup(1200, 600)
screen.colormode(255)
screen.tracer(0)
screen.listen()

text = Text()

paddle = Paddle()
ball = Ball()
brick = Brick()

screen.onkeypress(paddle.move_left, key="Left")
screen.onkeypress(paddle.move_right, key="Right")

game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(paddle) < 30:
        ball.y_bounce()
    if ball.xcor() > 590 or ball.xcor() < -595:
        ball.x_bounce()
    if ball.ycor() > 290:
        ball.y_bounce()
    if ball.ycor() < -290:
        ball.home()
        ball.y_bounce()
        text.lives -= 1
        if text.lives == 0:
            screen.clearscreen()
            screen.bgcolor("black")
            text.goto(x=0, y=0)
            text.write(f"Game Over!", False, align="center", font=("Arial", 30, "normal"))
            game_is_running = False
            screen.exitonclick()
        else:
            text.clear()
            text.write(f"Score: {text.score}\nLives: {text.lives}", False, align="Left", font=("Arial", 20, "normal"))
    for _brick in brick.bricks:
        if ball.distance(_brick) < 45:
            _brick.hideturtle()
            text.score += 1
            text.clear()
            text.write(f"Score: {text.score}\nLives: {text.lives}", False, align="Left", font=("Arial", 20, "normal"))
            brick.bricks.remove(_brick)
            ball.y_bounce()
