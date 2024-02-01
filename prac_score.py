from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        with open("deba_file.txt" , "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} high score:{self.high_score}", align = "center" , font =("arial" , 24 , "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("deba_file.txt" , "w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score += 1
        self.update_score()