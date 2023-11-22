from turtle import Turtle

ballSize = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(ballSize,ballSize)
        self.color('white')
        self.goto(0,0)
        self.penup()
    
    def move(self):
        