from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game!")
screen.tracer(0)

rightPaddle = Paddle((350,0))
leftPaddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(rightPaddle.moveUp, "Up")
screen.onkey(rightPaddle.moveDown, "Down")

screen.onkey(leftPaddle.moveUp, "w")
screen.onkey(leftPaddle.moveDown, "s")


    
gameIsOn = True
while gameIsOn:
    screen.tracer(1)
    ball.move()

screen.exitonclick()