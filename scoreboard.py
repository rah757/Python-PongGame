from turtle import Turtle

font = ("Courier", 70, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.updateScore()
        
    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align='center', font = font)
        self.goto(100, 200)
        self.write(self.rightScore, align='center', font = font)
        self.goto(0, 200)
        self.write("-", align='center', font = font)
    
    def lPoint(self):
        self.leftScore += 1
        self.updateScore()
    
    def rPoint(self):
        self.rightScore += 1
        self.updateScore()
    