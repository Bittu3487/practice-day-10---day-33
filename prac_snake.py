from turtle import Turtle , Screen
positions = [(0,0),(-20,0),(-40,0)]
new_segment = []
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.new_segment = []
        self.create_snake()
        self.head = self.new_segment[0]
    def create_snake(self):
        for position in positions:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.new_segment.append(segment)
    def reset(self):
        for seg in self.new_segment:
            seg.goto(1000 , 1000)
        self.new_segment.clear()
        self.create_snake()
        self.head = self.new_segment[0]
    def extend(self):
        self.add_segment(self.new_segment[-1].position())
    def move(self):
         for seg_num in range(len(self.new_segment)-1 , 0 , -1):
            x_position = self.new_segment[seg_num - 1].xcor()
            y_position = self.new_segment[seg_num - 1].ycor()
            self.new_segment[seg_num].goto(x_position,y_position)
         self.head.forward(20)
    def up(self):
        if self.head != down:
            self.head.setheading(up)
    def down(self):
        if self.head != up:
            self.head.setheading(down)
    def left(self):
        if self.head != right:
            self.head.setheading(left)
    def right(self):
        if self.head != left:
            self.head.setheading(right)
    