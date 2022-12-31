import turtle
turtle.pensize(2)
turtle.speed(55555)

width=100
height=40
turtle.color('blue')
turtle.pendown()
turtle.begin_fill()
for l in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.clear()
turtle.pendown()
turtle.begin_fill()
size=100
turtle.color('green')
for l in range(4):
    turtle.forward(size)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.done()
