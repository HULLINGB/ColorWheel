import turtle
import time

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
time.sleep(10)
turtle.hideturtle()
