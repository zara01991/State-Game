from turtle import Turtle, Screen


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto (180,170)
        self.write ("Score: ",False, align="center", font = ('Arial', 25, 'normal'))
        self.s = 0
        self.goto (230,170)
        self.write (self.s ,False, align="center", font = ('Arial', 25, 'normal'))

    
    def add_score(self):
        self.undo()
        self.s += 1
        self.goto (230,170)
        self.write (self.s ,False, align="center", font = ('Arial', 25, 'normal'))