import turtle
import math
from random import *
import time

screen = turtle.Screen()
screen.setup(400, 800)
screen.bgcolor("black")
w = screen.window_width()
h = screen.window_height()

livesLeft = 3
x=0
roundOne = []
shots =[]
colorList = ['yellow', 'white', 'grey']
#Makes a lives counter
pen1 = turtle.Turtle()
pen1.color("white")
pen1.hideturtle()
pen1.up()
pen1.goto(-190,-360)
pen1.down()
pen1.write("Lives: " + str(livesLeft), False, 'left', font = ('Cooper Black', 11, 'bold'))
pen2= turtle.Turtle()
pen2.color("#ffffff")
pen2.hideturtle()
pen2.up()
pen2.goto(-190, -380)
pen2.write("Enemies Left: " + str(29-x), False, 'left', font = ('Cooper Black', 11, 'bold'))

# make a turtle that the user controls

me = turtle.Turtle()
me.shape('triangle')
me.color("#ff0000")
me.penup()
me.setx(0)
me.sety(-170)
me.setheading(90)


def moveMeUp():
    me.setheading(90)
    me.forward(10)
    me.setheading(90)
    
def moveMeRight():
    me.setheading(0)
    me.forward(10)
    me.setheading(90)
    
def moveMeLeft():
    me.setheading(180)
    me.forward(10)
    me.setheading(90)

def moveMeDown():
    me.setheading(270)
    me.forward(10)
    me.setheading(90)
    
# make a bunch of missile turtles
counter=0
row = 1
moveY = 0
shapE = "square"
sizE = 1
move = 0
for i in range(29):
    if i == 10:
        row = 2
        moveY = 30
        counter = 0
    elif i == 20:
        row = 1.5
        moveY = 15
        counter = 20
        shapE = "triangle"
        sizE = 0.5
        move = 30
    t = turtle.Turtle()
    t.turtlesize(sizE)
    t.penup()
    t.shape(shapE)
    t.color(choice(colorList))
    t.setx(-w/2 + 17 + counter)
    t.sety(180 - moveY)
    t.setheading(270 + move)
    roundOne.append(t)
    counter += 40

def shot():
    shooter = turtle.Turtle()
    shooter.turtlesize(0.5)
    shooter.up()
    shooter.shape("circle")
    shooter.setheading(90)
    shooter.color("#8888ee")
    shooter.goto(me.pos())
    shots.append(shooter)

turtle.tracer(0,0)

decider = 0
while decider == 0:
    deleteTurtleList = []
    deleteBulletList = []
    trackOnTurtles = []
    for t in roundOne:
        t.forward(2)
        trackOnTurtles.append(t)
        if t.xcor() > w/2:
            t.setheading(270-30)
        if t.ycor() < -h/2:
            t.sety(h/2)
        if t.xcor() < -w/2:
            t.setheading(270+30)
        if math.sqrt((t.xcor()-me.xcor())**2 + (t.ycor()-me.ycor())**2) < 15:
            livesLeft = livesLeft - 1
            pen1.clear()
            pen1.up()
            pen1.goto(-190,-360)
            pen1.down()
            pen1.write("Lives: " + str(livesLeft), False, 'left', font=('Cooper Black', 11, 'bold'))
            x = x + 1
            pen2.clear()
            pen2.hideturtle()
            pen2.up()
            pen2.goto(-190, -380)
            pen2.write("Enemies Left: " + str(29-x), False, 'left', font = ('Cooper Black', 11, 'bold'))
            deleteTurtleList.append(t)
            if livesLeft == 0:    
                decider = 1
                continue
    for bull in shots:
        bull.forward(2.2)
        if bull.ycor() > h/2:
            deleteBulletList.append(bull)
        for t in trackOnTurtles:
            if math.sqrt((bull.xcor()-t.xcor())**2 + (bull.ycor()-t.ycor())**2) < 15:
                x = x + 1
                pen2.clear()
                pen2.hideturtle()
                pen2.up()
                pen2.goto(-190, -380)
                pen2.write("Enemies Left: " + str(29-x), False, 'left', font = ('Cooper Black', 11, 'bold'))
                deleteBulletList.append(bull)
                deleteTurtleList.append(t)
    

    
    
    if livesLeft == 0:
        screen.clear()
        screen.bgcolor("Black")
        pen1.setpos(0, 250)
        pen1.write("Game Over......", False, 'center', font=('Cooper Black', 35, 'bold'))
        decider = 1
        
    if x == 29:
        screen.clear()
        screen.bgcolor("Black")
        pen1.setpos(0, 250)
        pen1.write("YOU WIN!", False, 'center', font=('Cooper Black', 35, 'bold'))
        decider = 1
        
    for t in deleteTurtleList:
        roundOne.remove(t)
        t.hideturtle()        
    for bull in deleteBulletList:
        shots.remove(bull)
        bull.hideturtle()
        
    turtle.update()
    screen.onkey(shot, ' ')
    screen.onkey(moveMeUp, 'Up')
    screen.onkey(moveMeLeft, 'Left')
    screen.onkey(moveMeRight, 'Right')
    screen.onkey(moveMeDown, 'Down')
    screen.listen()