import turtle as trtl

# make the spider's body

spider = trtl.Turtle()
spider.pensize(41)
spider.color("black")
spider.circle(30)

# configure legs

legs = 4
leg_length = 70
leg_direction = 120 / legs
spider.pensize(5)
limit = 0

# make the spider's legs

while (limit < legs):
  spider.penup()
  spider.goto(0,20)
  spider.setheading(leg_direction*limit+90)
  spider.pendown()
  spider.circle(70,140)
  spider.penup()
  limit = limit + 1
limit = 0
leg_direction = -120 / legs
while (limit < legs):
  spider.penup()
  spider.goto(0,20)
  spider.setheading(leg_direction*limit+270)
  spider.pendown()
  spider.circle(70,-140)
  spider.penup()
  limit = limit + 1
spider.hideturtle()
wn = trtl.Screen()

# make the head

spider.penup()
spider.goto(25,-45)
spider.pendown()
spider.begin_fill()
spider.circle(40)
spider.end_fill()

# make the lil eyes

spider.penup()
spider.color("red")
spider.goto(15,-15)
spider.pensize(10)
spider.pendown()
spider.circle(5)

spider.penup()
spider.goto(-15,-15)
spider.pensize(10)
spider.pendown()
spider.circle(5)
