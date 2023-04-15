from turtle import Turtle, Screen

class State (Turtle):
    def __init__(self,x, y , answer):
        super().__init__()
        
        #state = Turtle()
        self.hideturtle()
        self.penup()
        self.x_cor = x
        self.y_cor = y
        self.answer =answer
        


    def display(self):
        self.goto(self.x_cor,self.y_cor)
        self.write(self.answer,False, align="center", font = ('Arial', 15, 'normal'))
        
