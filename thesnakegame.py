from turtle import *
from snake import Snake
import time
from food import Food
from scoreboard import scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")  # Capitalize "Up" for consistency
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    # Collision detection with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # Collision detection with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # Adjust distance for more accuracy
            game_is_on = False
            scoreboard.game_over()
            

screen.exitonclick()
