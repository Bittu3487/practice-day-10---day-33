from turtle import Turtle
import random
colors = ["red" , "yellow" , "green" , "blue" , "purple" , "black"]
move_distance = 5
move_increment = 10
class Car:
    def __init__(self):
        self.all_car = []
        self.car_speed = move_distance
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250,250)
            new_car.goto(300 , random_y)
            self.all_car.append(new_car)
    def move(self):
        for car in self.all_car:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += move_increment
