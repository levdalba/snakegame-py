from turtle import Turtle


class Snake:
    def __init__(self, positions):
        self.segments = []
        self.create_snake(positions)
        self.head = self.segments[0]

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
        self.head.forward(20)

    def extend(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
