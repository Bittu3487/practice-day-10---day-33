from turtle import Turtle , Screen
from prac_paddle import Paddle
from prac_ball import Ball
from practice_score_board import ScoreBoard
import time
ball = Ball()
screen = Screen()
scoreboard = ScoreBoard()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350 ,0))
l_paddle = Paddle((-350 , 0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()  
screen.exitonclick()