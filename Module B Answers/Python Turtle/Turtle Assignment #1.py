import turtle
import random
pen = turtle.Turtle()
pen.speed("fastest")

def movePen(xPos, yPos):
    pen.pu()
    pen.fd(xPos)
    pen.right(90)
    pen.fd(yPos)
    pen.left(90)
    pen.pd()

def blueBox(color, size):
    pen.pd()
    pen.color(color)
    for i in range(4):
        pen.fd(size)
        pen.right(90)
    pen.pu()
    

def questionOne():
    movePen(0, 0)
    blueBox("blue", 40)
    movePen(20, 60)
    blueBox("blue", 40)
    movePen(80, 0)
    blueBox("blue", 40)
    movePen(-100, -60)
    blueBox("blue", 40)
    
#Bottom Left: 1
#Bottom Right: 2
#Top Right: 3
#Top Left: 4
def modifiedBlueBox(x, y, color, size, side): 
    pen.pu()
    pen.setposition(x, y)
    pen.pd()
    pen.color(color)
    for i in range(4):
        pen.fd(size)
        pen.right(90)
    if (side == 1):
        pen.begin_fill()
        pen.right(45)
        pen.fd(size + size/ 2.5)
        pen.left(225)
        pen.fd(size)
        pen.right(90)
        pen.fd(size)
        pen.right(90)
        pen.end_fill()
    if(side == 2):
        pen.begin_fill()
        pen.fd(size)
        pen.right(135)
        pen.fd(size + size/ 2.5)
        pen.left(-225)
        pen.fd(size)
        pen.left(90)
        pen.fd(size)
        pen.left(90)
        pen.fd(size)
        pen.right(180)
        pen.end_fill()
    if(side == 3):
        pen.begin_fill()
        pen.right(45)
        pen.fd(size + size/ 2.5)
        pen.left(135)
        pen.fd(size)
        pen.left(90)
        pen.fd(size)
        pen.right(180)
        pen.end_fill()
    if(side == 4):
        pen.begin_fill()
        pen.right(90)
        pen.fd(size)
        pen.left(-225)
        pen.fd(size + size/ 2.5)
        pen.left(135)
        pen.fd(size)
        pen.right(180)
        pen.end_fill()
    
xPos = 0
yPos = 0
size = 50
setOne = True
setOneFirst = True
setTwoFirst = True
    
for i in range(8):
    for j in range(8):
        if(setOne):
            if(setOneFirst):
                modifiedBlueBox(xPos, yPos, "black", size, 2)
                setOneFirst = False
            else:
                modifiedBlueBox(xPos, yPos, "black", size, 3)
                setOneFirst = True
        if(not(setOne)):
            if(setTwoFirst):
                modifiedBlueBox(xPos, yPos, "black", size, 1)
                setTwoFirst = False
            else:
                modifiedBlueBox(xPos, yPos, "black", size, 4)
                setTwoFirst = True
        xPos += size
    
    if(setOne):
        setOne = False
    else: 
        setOne = True
    yPos -= size
    xPos = 0
