# import turtle as t
# import random
# t.colormode(255)
# class RandomWalk:
#     def __init__(self):
#         self.screen = t.Screen()
#         self.tim = t.Turtle()
#         self.tim.speed("fastest")
#     def random_color(self):
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#         my_tuple = (r,g,b)
#         return(my_tuple)
#     def spiro_graph(self , size_gap):
#         for _ in range(int(360/size_gap)):
#             self.tim.color(self.random_color())
#             self.tim.circle(100)
#             self.tim.setheading(self.tim.heading() + size_gap)
# randomwalk = RandomWalk()
# randomwalk.spiro_graph(5)
# from turtle import Turtle , Screen
# tim = Turtle()
# screen = Screen()
# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def turn_right():
#      new_heading = tim.heading() - 10
#      tim.setheading(new_heading)
# def screen_clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(move_forwards , "w")
# screen.onkey(move_backward , "s")
# screen.onkey(turn_left , "a")
# screen.onkey(turn_right , "d")
# screen.onkey(screen_clear , "c")

# screen.exitonclick()
from turtle import Turtle , Screen
import random
screen = Screen()
screen.setup(500 , 400)
user_bet = screen.textinput(title = "user bet", prompt = "which colour turtle win the race?")
colors = ["red" , "blue" , "yellow" , "purple" , "black" , "orange"]
y_position = [-70 , -40 , -10 ,20 , 50 , 80 ]
all_turtle = []
for turtle_index in range(0,6):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(tim)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
           is_race_on = False
           winning_color = turtle.pencolor()
           if winning_color == user_bet:
              print(f"you have won the {winning_color} turtle is the winner")
           else:
                print(f"you have loose the game winning color is {winning_color}") 
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)