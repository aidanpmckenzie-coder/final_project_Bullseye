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
display_screen = "menu"
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


# Archery Board Rings (Colors & radius)
FIRST_RING_COLOR = "white"
SECOND_RING_COLOR = "black"
THIRD_RING_COLOR = "blue"
FOURTH_RING_COLOR= "red"
BULLSEYE_RING_COLOR = "yellow"

FIRST_RING_RADIUS = 100
SECOND_RING_RADIUS = 80
THIRD_RING_RADIUS = 60
FOURTH_RING_RADIUS = 40
BULLSEYE_RING_RADIUS = 20


# Archery Board (Game Screen)
def draw_archery_board():
    pen.clear()
    colors = [FIRST_RING_COLOR, SECOND_RING_COLOR, THIRD_RING_COLOR, FOURTH_RING_COLOR, BULLSEYE_RING_COLOR]
    sizes = [FIRST_RING_RADIUS, SECOND_RING_RADIUS, THIRD_RING_RADIUS, FOURTH_RING_RADIUS, BULLSEYE_RING_RADIUS]
    for i in range(5):
        pen.goto(0, -sizes[i])
        pen.color(colors[i])
        pen.begin_fill()
        pen.circle(sizes[i])
        pen.end_fill()
    pen.color("black")


# Information (Information Screen)
def draw_info():
    pen.clear()
    # How to Play 
    pen.goto(0, 125)
    pen.write("How to Play", align="center",font=("Arial", 20))
    pen.goto(0, 80)
    pen.write("Welcome to Archery! The rules of the game are simple, rack up points by hitting a ring on the archery board.", align="center", font=("Arial", 14))
    pen.goto(0,60)
    pen.write("Hitting the board will get you points, and points increase the closer you are to the bullseye", align="center", font=("Arial", 14))
    pen.goto(0,40)
    pen.write("However, it is not as simple as just clicking on the bullseye, as wind will play a factor in this challenge.", align="center", font=("Arial", 14))
    pen.goto(0,20)
    pen.write("The game consists of 2 players, the player with the most points after each player runs out of arrows, wins!", align="center", font=("Arial", 14))
    pen.goto(0,-20)
    # Start the Game
    pen.write("Click anywhere on the screen to begin!", align="center", font=("Arial", 14))


# Clicking function
# This function determines which screen will be displayed to the user after clicking a certain button or action
# For the game, it determines what will appear on the screen after the player interacts with the game
def click(x, y):
    global display_screen
    # Main Menu
    if display_screen == "menu":
        if start_button.clicked(x, y):
            display_screen = "game"
            draw_archery_board()
        elif info_button.clicked(x, y):
            display_screen = "info"
            draw_info()

    # Information screen
    elif display_screen == "info":
        display_screen = "game"
        draw_archery_board()


# Running
screen.onclick(click)
draw_menu()
turtle.done()