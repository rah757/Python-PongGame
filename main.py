from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game!")
screen.tracer(0)

rightPaddle = Paddle((350,0))
leftPaddle = Paddle((-350,0))

ball = Ball()

rightPaddleScore = 0
leftPaddleScore = 0

screen.listen()

screen.onkey(rightPaddle.moveUp, "Up")
screen.onkey(rightPaddle.moveDown, "Down")

screen.onkey(leftPaddle.moveUp, "w")
screen.onkey(leftPaddle.moveDown, "s")


gameIsOn = True
while gameIsOn:
    time.sleep(0.069)
    screen.update()
    ball.move()
    # Detect collision with paddles
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bouncePaddle()
    # Detect ball out of bounds 
    # Right paddle miss
    if ball.xcor() > 400:
        rightPaddleScore += 1
        ball.reset()
    # Left paddle miss
    elif ball.xcor() < -400:
        leftPaddleScore += 1
        ball.reset()

screen.exitonclick()