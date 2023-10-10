from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color="blue", points=1):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.points = points
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
