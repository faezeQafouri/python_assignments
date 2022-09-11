

import turtle 
import random


s = turtle.getscreen()
turtle.title("My Turtle Program ^---^")
t = turtle.Turtle()
# side  = input("Enter the side of your desier shape:")
# color = input("Enter the color of your desier shape:")

numberOfSides = int(input('Enter the number of sides of a polygon: '))
lengthOfSide = int(input('Enter the length of a side of a polygon: '))
colorofshape = input('Enter the color of a polygon: ')


exteriorAngle = 360/numberOfSides
t.pencolor(colorofshape)
t.fillcolor(colorofshape)
t.begin_fill()
for i in range(numberOfSides):
    
    t.forward(lengthOfSide)
    t.right(exteriorAngle)


t.end_fill() 
turtle.done()




#change backgroud on click
# color = ['purple', 'pink', 'red', 'yellow', 'green', 
#        'black', 'blue', 'orange',] 
# def fun(x, y): 
#     global color
#     r = random.randint(0, 7) 
#     scr.bgcolor(color[r]) 
# scr = turtle.Screen() 
# scr.setup(500, 400) 
# turtle.onscreenclick(fun)
# turtle.done()


