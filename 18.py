# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(5):
#     tim.forward(30)
#     tim.penup()
#     tim.forward(30)
#     tim.pendown()
#     tim.forward(30)
import turtle as t
import random
t.colormode(255)
class Drawer:
    def __init__(self):
        self.screen = t.Screen()
        self.tim = t.Turtle()
        self.tim.speed("fastest")
    def draw_shape(self,num_slide):
        angel = 360/num_slide
        for _ in range(num_slide):
            self.tim.forward(100)
            self.tim.right(angel)
    def add_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        my_tuple = (r,g,b)
        return(my_tuple)
    def draw_shapes(self , min_slide , max_slide):
        for num_shape in range(min_slide , max_slide +1):
            self.tim.color(self.add_color())
            self.draw_shape(num_shape)
    def exiton_click(self):
        self.screen.exitonclick()
drawer = Drawer()
drawer.draw_shapes(3,10)
drawer.exiton_click()