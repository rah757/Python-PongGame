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
        self.movementDirection = 1
        self.movementSpeed = 0.069
    
    def move(self):
        new_x = self.xcor() + self.xMovement * self.movementDirection
        new_y = self.ycor() + self.yMovement * self.movementDirection
        self.goto(new_x, new_y)
        self.bounce()
        
    def bounce(self):                                   
        if self.ycor() > 275 or self.ycor() < -275:         # Detect collision with wall and bounce it off
            self.yMovement*= -1             # multiply it w -1 to bounce it off
        
    def bouncePaddle(self):
        self.xMovement*=-1
        
    def reset(self):
        self.goto(0,0)
        self.movementDirection *= -1
        self.movementSpeed *= 0.9
        self.move()
        