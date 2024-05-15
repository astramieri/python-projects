from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


LIMIT = 290

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # detect collision with wall
    if snake.head.xcor() > LIMIT or snake.head.xcor() < -LIMIT or snake.head.ycor() > LIMIT or snake.head.ycor() < -LIMIT:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        position = (segment.xcor(), segment.ycor())
        if snake.head.distance(position) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
