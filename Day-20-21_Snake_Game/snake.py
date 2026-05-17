from turtle import Turtle
START_POSITION =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self) :
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in START_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segment[-1].xcor(), self.segment[-1].ycor())
        self.segment.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segment[0].setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.segment[0].setheading(0)