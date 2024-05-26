from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My first Snake Game!")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()





