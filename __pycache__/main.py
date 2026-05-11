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
SCREEN_BACKGROUND_COLOR = "linen"
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
display_screen = "menu"
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)

# Turtle Pens
# Some pens only used once, others constantly update screen

# Menu, Info, Results pen
menu_pen = turtle.Turtle()
menu_pen.hideturtle()
menu_pen.speed(0)
menu_pen.penup()

# Archery Board pen
archery_board_pen = turtle.Turtle()
archery_board_pen.hideturtle()
archery_board_pen.speed(0)
archery_board_pen.penup()

# Game Text pen (changing each turn)
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.speed(0)
text_pen.penup()

# Arrow Shots pen
shot_pen = turtle.Turtle()
shot_pen.hideturtle()
shot_pen.speed(0)
shot_pen.penup()


# Game Stats (While Playing game)
player = 1 # player 1's turn
arrows = 10 # each player gets 5 arrows
wind_x = 0 # x coordinate to aim for
wind_y = 0 # y coordinate to aim for
player_one_score = 0
player_two_score = 0


# Main Menu
start_button = Button(0, 20, "START", menu_pen)
info_button = Button(0, -40, "INFO", menu_pen)
def draw_menu():
    menu_pen.clear()
    menu_pen.goto(0, 100)
    menu_pen.write("ARCHERY", align="center", font=("Arial", 24))
    start_button.draw()
    info_button.draw()


# Archery Board Rings (Colors & radius)
OUTLINE_RING_COLOR = "black"
FIRST_RING_COLOR = "white"
SECOND_RING_COLOR = "black"
THIRD_RING_COLOR = "blue"
FOURTH_RING_COLOR= "red"
BULLSEYE_RING_COLOR = "yellow"

OUTLINE_RING_RADIUS = 100.6
FIRST_RING_RADIUS = 100
SECOND_RING_RADIUS = 80
THIRD_RING_RADIUS = 60
FOURTH_RING_RADIUS = 40
BULLSEYE_RING_RADIUS = 20

# Arrow on Screen (shot taken)
ARROW_SHOT_RADIUS = 8

# Archery Board (Game Screen)
def draw_archery_board():
    archery_board_pen.clear()
    colors = [OUTLINE_RING_COLOR,FIRST_RING_COLOR, SECOND_RING_COLOR, THIRD_RING_COLOR, FOURTH_RING_COLOR, BULLSEYE_RING_COLOR]
    sizes = [OUTLINE_RING_RADIUS, FIRST_RING_RADIUS, SECOND_RING_RADIUS, THIRD_RING_RADIUS, FOURTH_RING_RADIUS, BULLSEYE_RING_RADIUS]
    for i in range(6):
        archery_board_pen.goto(0, -sizes[i])
        archery_board_pen.color(colors[i])
        archery_board_pen.begin_fill()
        archery_board_pen.circle(sizes[i])
        archery_board_pen.end_fill()
    archery_board_pen.color("black")

# Wind (The wind recommends the coordinate that the player should aim at, changes after each shot)
def wind():
    global wind_x, wind_y
    wind_x = random.randint(-240,240)
    wind_y = random.randint(-240,240)

    # Preventing easy shots 
    while -20 < wind_x < 20 or -20 < wind_y < 20:
        wind_x = random.randint(-240,240)
        wind_y = random.randint(-240,240)

# Game Text
def draw_text():
    text_pen.clear()
    # Player (1 for now)
    text_pen.goto(-220, 220)
    text_pen.write(f"Player: {player}",font=("Arial", 12))

    # Arrows (Maximum 5)
    text_pen.goto(-220, 190)
    text_pen.write(f"Arrows: {arrows}",font=("Arial", 12))

    # Wind
    text_pen.goto(-80, -230)
    text_pen.write(f"Wind: ({wind_x}, {wind_y})",font=("Arial", 12))

    # Scores
    text_pen.goto(140, 220)
    text_pen.write(f"P1: {player_one_score}", font=("Arial", 12))

    text_pen.goto(140, 190)
    text_pen.write(f"P2: {player_two_score}", font=("Arial", 12))

# Score
def score(x,y):
    distance = math.dist((x, y), (0, 0))  # shot distance from bullseye center
    # Hits Bullseye
    if distance <= BULLSEYE_RING_RADIUS:
        return 10
    
    # Hits Fourth Ring 
    elif distance <= FOURTH_RING_RADIUS:
        return 8
    
    # Hits Third Ring 
    elif distance <= THIRD_RING_RADIUS:
        return 6
    
    # Hits Second Ring 
    elif distance <= SECOND_RING_RADIUS:
        return 4
    
    # Hits First Ring 
    elif distance <= FIRST_RING_RADIUS:
        return 2
    
    # Does not Hit Archery Board
    else:
        return 0


# Information (Information Screen)
def draw_info():
    menu_pen.clear()
    # How to Play 
    menu_pen.goto(0, 190)
    menu_pen.write("How to Play", align="center",font=("Arial", 20))
    menu_pen.goto(0, 160)
    menu_pen.write("Welcome to Archery! The rules of the game are simple, rack up points by hitting a ring on the archery board.", align="center", font=("Arial", 14))
    menu_pen.goto(0,140)
    menu_pen.write("Hitting the board will get you points, and points increase the closer you are to the bullseye", align="center", font=("Arial", 14))
    menu_pen.goto(0,120)
    menu_pen.write("However, it is not as simple as just clicking on the bullseye, as wind will play a factor in this challenge.", align="center", font=("Arial", 14))
    menu_pen.goto(0,100)
    menu_pen.write("The game consists of 2 players, the player with the most points after each player runs out of arrows, wins!", align="center", font=("Arial", 14))
    
    # Score Distribution
    menu_pen.goto(0, 80)
    menu_pen.write("Bullseye: 10 Points", align="center",font=("Arial", 12))
    menu_pen.goto(0, 60)
    menu_pen.write("Red: 8 Points", align="center",font=("Arial", 12))
    menu_pen.goto(0, 40)
    menu_pen.write("Blue: 6 points", align="center",font=("Arial", 12))
    menu_pen.goto(0, 20)
    menu_pen.write("Black: 4 points", align="center",font=("Arial", 12))
    menu_pen.goto(0, 0)
    menu_pen.write("White: 2 points", align="center",font=("Arial", 12))
    menu_pen.goto(0, -20)
    menu_pen.write("Miss: 0 Points", align="center",font=("Arial", 12))

    # Hints
    menu_pen.goto(0,-70)
    menu_pen.write("Hint: The radius of the archery board is 100", align="center", font=("Arial", 10))
    menu_pen.goto(0,-90)
    menu_pen.write("Hint: The center of the archery board is the origin (0,0)", align="center", font=("Arial", 10))
    menu_pen.goto(0,-110)
    menu_pen.write("Hint: It is recommended that you direct your aim at the wind coordinates", align="center", font=("Arial", 10))

    # Start the Game
    menu_pen.goto(0,-185)
    menu_pen.write("Click anywhere on the screen to begin!", align="center", font=("Arial", 13))

# Game Results
def draw_game_results():
    menu_pen.clear()
    archery_board_pen.clear()
    shot_pen.clear()
    text_pen.clear()
    # Finding the Winner
    if player_one_score > player_two_score:
        result = "Player 1 Wins!"
    elif player_two_score > player_one_score:
        result = "Player 2 Wins!"
    else: 
        result = "Tie Game!"
    
    # Results Displayed
    menu_pen.goto(0,80)
    menu_pen.write(result,align="center",font=("Arial", 24))
    menu_pen.goto(0,30)
    menu_pen.write(f"P1: {player_one_score}   P2: {player_two_score}",align="center",font=("Arial", 16))

    # Return to Main Menu
    menu_pen.goto(0, -50)
    menu_pen.write("Click anywhere to return to menu!",align="center",font=("Arial", 12))


# Play the Game (Shooting)
def shoot(x,y):
    global player, arrows, player_one_score, player_two_score, display_screen

    # Shooting using the wind (corrects shot)
    x -= wind_x
    y -= wind_y

    # Player arrow shots appear on screen in different colors to indicate which player shot where
    if player == 1:
        shot_color = "green"

    else:
        shot_color = "magenta"

    # Draw shot on the screen
    shot_pen.goto(x, y)
    shot_pen.dot(ARROW_SHOT_RADIUS, shot_color)

    # Updating Points
    points = score(x,y)
    if player == 1:
        player_one_score += points
    else:
        player_two_score += points
    
    # Updating Game Stats after each shot
    arrows -= 1

    #alternate shots
    if player == 1:
        player = 2
    else: 
        player = 1

    # Update 
    wind()
    draw_text()

    # End the game
    if arrows == 0:
        display_screen = "game_over"
        draw_game_results()


# Clicking function
# This function determines which screen will be displayed to the user after clicking a certain button or action
# For the game, it determines what will appear on the screen after the player interacts with the game
def click(x, y):
    global display_screen, player, arrows, player_one_score, player_two_score
    # Main Menu
    if display_screen == "menu":
        if start_button.clicked(x, y):
            display_screen = "game"
            menu_pen.clear()
            shot_pen.clear()
            text_pen.clear()
            wind()
            draw_archery_board()
            draw_text()

        elif info_button.clicked(x, y):
            display_screen = "info"
            draw_info()

    # Information screen
    elif display_screen == "info":
        display_screen = "game"
        menu_pen.clear()
        draw_archery_board()
        wind()
        draw_text()

    # Begin the Game
    elif display_screen == "game":
        shoot(x,y)

    # Game Results and Reset
    elif display_screen == "game_over":
        menu_pen.clear()
        archery_board_pen.clear()
        shot_pen.clear()
        text_pen.clear()
        player = 1
        arrows = 10
        player_one_score = 0
        player_two_score = 0
        display_screen = "menu"
        draw_menu()


# Running
screen.onclick(click)
draw_menu()
turtle.done()