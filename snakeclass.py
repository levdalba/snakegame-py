from turtle import Turtle


class Snake:
    def __init__(self, positions):
        self.segments = []
        self.create_snake(positions)

    def up(self):
        self.segments[0].setheading(90)

    def create_snake(self, positions):
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(pos)
            self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
