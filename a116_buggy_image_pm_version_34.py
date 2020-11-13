# a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.goto(0,-25)
ladybug.pensize(40)
ladybug.circle(5)

# configure legs

legs = 4
leg_length = 50
leg_direction = -120 / legs
ladybug.pensize(5)
limit = 0

# make the ladybug's legs

while (limit < legs):
  ladybug.goto(0,-55)
  ladybug.setheading(leg_direction*limit+45)
  ladybug.forward(leg_length)
  limit = limit + 1
limit = 0
leg_direction = 120 / legs
while (limit < legs):
  ladybug.goto(0,-55)
  ladybug.setheading(leg_direction*limit-220)
  ladybug.forward(leg_length)
  limit = limit + 1
ladybug.hideturtle()
wn = trtl.Screen()

# and body
ladybug.penup()
ladybug.setheading(180)
ladybug.goto(0,-35) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0,-15)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -75
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = xpos + 5
  ypos = ypos + 25
  num_dots = num_dots + 1

ladybug.hideturtle()
