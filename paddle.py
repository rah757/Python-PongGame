from turtle import Turtle
paddleWidth = 6
paddleLength = 1


class Paddle(Turtle):
    def __init__(self,coords):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(paddleWidth, paddleLength)
        self.penup()
        self.goto(coords)
            
    def moveUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def moveDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
