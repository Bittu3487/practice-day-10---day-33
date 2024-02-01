from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}" , align = "Left" , font=("courier" , 24 , "normal"))
        
    def level_increase(self):
        self.level += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game is Over" , align = "center" , font=("courier" , 24 , "normal"))