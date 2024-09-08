import turtle
turtle.Screen().bgcolor("Orange")
t=turtle.Turtle()
t.shape("turtle")
t.color("red")
for c in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
for c in range(3):
    t.forward(200)
    t.right(120)

turtle.done()