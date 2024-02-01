from turtle import Turtle , Screen
from p import Player
from c import Car
from s import ScoreBoard
import time
screen = Screen()
screen.tracer(0)
screen.setup(600,600)
screen.title("turtle crossing game")
player = Player()
car = Car()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(player.go_up,"Up")







game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for n_car in car.all_car:
        if n_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish():
        player.go_start()
        car.level_up()
        scoreboard.level_increase()
screen.exitonclick()