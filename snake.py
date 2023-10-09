from turtle import Screen, Turtle
import time

screen = Screen()

screen.bgcolor("black")

screen.setup(width=600, height=600)

screen.tracer(0)

segments = []

positions = [(0, 0), (20, 0), (40, 0)]
for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(pos)
    segments.append(new_turtle)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for segment in segments:
        segment.forward(20)
        screen.update()


screen.exitonclick()
