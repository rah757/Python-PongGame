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
        self.xMovement = 10
        self.yMovement = 10
    
    def move(self):
        new_x = self.xcor() + self.xMovement
        new_y = self.ycor() + self.yMovement
        self.goto(new_x, new_y)
        self.bounce()
        
    def bounce(self):
        if self.ycor() > 275 or self.ycor() < -275:
            self.yMovement*= -1
