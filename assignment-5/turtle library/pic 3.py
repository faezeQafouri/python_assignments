#Program to draw a Rainbow using turtle in Python  
# Importing the turtle package  
import turtle  
  
# Defining a screen object for turtle  
scr = turtle.Screen()  
  
# Defining a turtle instance/object(pen)  
ttl = turtle.Turtle()  
  
# Initialising a function to draw a semicircle  
# with a dynamic radius and color  
def semi_circle(clr, rad, val):  
  
    # Setting the fill color of the semicircle to be drawn  
    ttl.color(clr)  
  
    # Drawing a circle  
    ttl.circle(rad, -180)  
  
    # Moving the turtle into the air  
    ttl.up()  
  
    # Moving the turtle to a given position/coordinates  
    ttl.setpos(val, 0)  
  
    # Moving the turtle back to the ground  
    ttl.down()  
  
    ttl.right(180)  
  
  
# Setting the colors for drawing the Rainbow  
clr = ['violet', 'indigo', 'blue',  
    'green', 'yellow', 'orange', 'red']  
  
# Set a value for the size of the screen features  
scr.setup(800, 600)  
  
# Setting the screen background color to black  
scr.bgcolor('black')  
  
# Setting the various turtle features  
ttl.right(90)  
ttl.width(11)  
ttl.speed(8)  
  
# for loop to draw 7 semicircles  
for j in range(7):  
    semi_circle(clr[j], 10*(  
    j + 8), -10*(j + 1))  
  
# Hiding the turtle  
ttl.hideturtle()  