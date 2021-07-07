# Hermon

# import required modules
import random
import turtle
import time

delay = 0.2 #TODO change this. what does it do?
score = 0
high_score = 0



# Creating a window screen
screen = turtle.Screen()
screen.title("Snake game") # TODO put a name in the parenthesis
screen.bgcolor("#4181f5") #TODO you need to add a color inside parenthesis
# the width and height can be put as user's choice
screen_width = int(input("What do you want the screen width to be?"))
screen_height =  int(input("What do you want to screen height to be?"))
length = int(input("What do you want the length to be?"))
screen.setup(width=screen_width, height=screen_height) 
#TODO: modify this, and use the input function to ask the user what size they want. 
# save those values and set it to the size of the window
screen.tracer(0)




# head of the snake
head = turtle.Turtle()
head.shape("square")  #TODO pick a shape for the head
head.color("#e20039")     #TODO pick a color for the head
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
# TODO make an array of 5 colors and randomly pick one. make sure it doesn't blend into your background
# Green, white, redish-black, orange, purple
colors = random.choice(["#6cfd00", "#fffef4", "#680118", "#ffa500", "#8d52eb"])#TODO random choice from your list.
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
foodX = (0, screen_width)
foodY = (0, screen_height)
food.goto(foodX, foodY) #TODO: replace x,y with numerical coordinate points




pen = turtle.Turtle()
pen.speed(0)
pen.shape()
pen.color()
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
#TODO write score

if(turtle.xcor() == foodX and turtle.ycor() == foodY):
    score += 1

# assigning key directions
# TODO: key directions for going up and down

def goleft():
	if head.direction != "right":
		head.direction = "left"


def goright():
	if head.direction != "left":
		head.direction = "right"

def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def move():
    if head.direction == "up":
        y = head.ycor()
        # TODO: what do we do after getting the coordinate? what does it mean to go up?
        y += 90
    if head.direction == "down":
        y = head.ycor()
        y -= 90
    if head.direction == "left":
        # TODO: get coordinate and move left
        x = head.xcor()
        x -= 90   
    if head.direction == "right":
        # TODO: get coordinate and move right
        x = head.xcor()
        x += 90


		

#TODO: call the functions on key press. example below, make sure you go left right and down.
screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(godown, "s")
screen.onkeypress(goleft, "a")
screen.onkeypress(goright, "d")

segments = []

while True:
    screen.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear

        score = 0

        delay = 0.1

    screen.clear()
    screen.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    if head.distance(food) <20:
        x = random.randint(290,-290)
        y = random.randint(290,-290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.color(colors)
        new_segment.speed(0)
        new_segment.shape(shapes)
        new_segment.penup
        segments.append(new_segment)
        










# Main Gameplay
#while True:
    #TODO: make the code for the main game iteration, and make sure you call your functions. have the snake move random
	
screen.mainloop()

