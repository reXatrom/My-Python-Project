import time
import sys
import turtle
import random

wh = turtle.Screen()
wh.setup(500,500)
wh.bgcolor('black')

myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.hideturtle()

colors = [
  'blue', 'red', 'yellow', 'orange', 'purple', 'magenta', 'pink', 'lime', 'green', 'gold', 'silver', 'violet'
]

def draw_fw(t):
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(random.choice(colors))
  d = random.randint(20,200)

  for i in range(36):
    t.forward(d)
    t.backward(d)
    t.right(50) #10 before

for i in range(12):
  draw_fw(myTurtle)

myTurtle.penup()
myTurtle.goto(0,10) #10 before
myTurtle.color('white')
myTurtle.write("Happy New Year!", align = "center", font = ("Times New Roman",24,"normal"))
#myTurtle.write("By reXatrom", align = "left", font = ("Times New Roman", 12,"italic"))

for m in "Happy New Year Famz.\nBy re X atrom.":
  sys.stdout.write(m)
  sys.stdout.flush()
  time.sleep(0.25)