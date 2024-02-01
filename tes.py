# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("inhale exhale")
#     def move(self):
#         print("moving in land")
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         num_eyes= 3
#     def move(self):
#         super().move()
#         print("moving in water")
#     def breathe(self):
#         super().breathe()
#         print("doing in under water")
# nemo = Fish()
# nemo.breathe()
# nemo.move()
# print(nemo.num_eyes)
# print(nemo.num_eyes)
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale exhale")

#     def move(self):
#         print("Moving on land")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         self.num_eyes = 3

#     def move(self):
#         super().move()
#         print("Moving in water")

#     def breathe(self):
#         super().breathe()
#         print("Doing it underwater")

# nemo = Fish()
# nemo.breathe()
# nemo.move()
# print(nemo.num_eyes)
# from turtle import Turtle,Screen
# import random
# screen = Screen()
# screen.setup(500 , 400)
# user_bet = screen.textinput(title = "tutrle game" , prompt = "choose your turtle color")
# y_position = [-70 , -40 , -10 , 20 , 50 , 80]
# colors = ["red" , "blue" , "purple" , "green" , "yellow" , "black"]
# all_turtle=[]
# for turtle_index in range(0,6):
#     turtle = Turtle(shape = "turtle")
#     turtle.penup()
#     turtle.color(colors[turtle_index])
#     turtle.goto(x=-230 , y = y_position[turtle_index])
#     all_turtle.append(turtle)
# game_is_on = True
# while game_is_on:
#     for new_turtle in all_turtle:
#         if new_turtle.xcor() > 230:
#             game_is_on = False
#             winning_color = new_turtle.pencolor()
#             if user_bet == winning_color:
#                 print(f" you have won the match and winning color is {winning_color}")
#             else:
#                 print(f"you loose the game , winnning color is {winning_color}")
#         new_turtle.forward(random.randint(0,10))
# screen.exitonclick()
# try:
#     file = open("data.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("data.txt" , "w")
#     file.write("something")
# except KeyError:
#     print("do not exist this key")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is a error i made this error")
# height = float(input("height"))
# weight = int(input("weight"))
# if height > 3:
#     raise ValueError("humman height should not over 3 meter")
# bmi = weight/height**2
# print(bmi)
print(max(0.2,0.4))