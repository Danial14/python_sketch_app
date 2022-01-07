# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from turtle import Turtle, Screen
def moveForward():
    tim.forward(20)
def moveBackward():
    tim.backward(20)
def clear():
    tim.clear()
    tim.setheading(0)
    tim.penup()
    tim.setposition(0.0, 0.0)
    tim.pendown()

def moveAntiClockwise():
    tim.left(10)

def moveClockWise():
    tim.right(10)

tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = moveForward)
screen.onkey(key = "s", fun = moveBackward)
screen.onkey(key = "c", fun = clear)
screen.onkey(key = "l", fun = moveAntiClockwise)
screen.onkey(key = "r", fun = moveClockWise)
screen.exitonclick()
