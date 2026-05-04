# Aidan McKenzie
# Computer Programming
# Period 5
# Final Project - Archery

# Imports
import turtle
import random
import math
from button import Button

# Screen
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

# Turtle Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()


# Main Menu
start_button = Button(0, 20, "START", pen)
info_button = Button(0, -40, "INFO", pen)
def draw_menu():
    pen.clear()
    pen.goto(0, 100)
    pen.write("ARCHERY", align="center", font=("Arial", 24))
    start_button.draw()
    info_button.draw()

# Clicking Main Menu
def click(x, y):
    if start_button.clicked(x, y):
        print("Start clicked")
    elif info_button.clicked(x, y):
        print("Info clicked")


# Running
screen.onclick(click)
draw_menu()
turtle.done()