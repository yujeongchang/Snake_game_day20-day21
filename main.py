from snake import Snake
from food import Food
from score_board import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My first Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()   #To listen user's key strokes.
screen.onkey(key= "Left", fun= snake.left)
screen.onkey(key= "Right", fun= snake.right)
screen.onkey(key= "Down", fun= snake.down)
screen.onkey(key= "Up", fun= snake.up)




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collision with food.
    if snake.head.distance(food) < 13:
        scoreboard.increase_score()
        snake.extend_tail()
        food.set_new_position()



    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()





