from turtle import Screen
import time
from food import Food
from snakeclass import Snake
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

snake = Snake(positions=[(0, 0), (-20, 0), (-40, 0)])
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
        or snake.check_collision()
    ):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
