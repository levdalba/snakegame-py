from turtle import Screen
import time

from snakeclass import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake(positions=[(0, 0), (-20, 0), (-40, 0)])
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

screen.exitonclick()
