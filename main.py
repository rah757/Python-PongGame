from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game!")
screen.tracer(0)

rightPaddle = Paddle((350,0))
leftPaddle = Paddle((-350,0))


screen.listen()
screen.onkey(rightPaddle.moveUp, "Up")
screen.onkey(rightPaddle.moveDown, "Down")

    
gameIsOn = True
while gameIsOn:
    screen.tracer(1)


screen.exitonclick()