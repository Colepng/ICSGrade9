import turtle as t
ts = t.Screen()
t.pensize(5)
z = 0
t.fillcolor("Green")
t.begin_fill()
while (z<3):
    t.fd(200)
    t.lt(120)
    z = z + 1
t.end_fill()
t.exitonclick()