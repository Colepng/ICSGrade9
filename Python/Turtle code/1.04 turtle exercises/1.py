import turtle as t
ts = t.Screen()
x = 0
while (x<2):
    t.pencolor("Pink")
    t.fd(150)
    t.right(90)
    t.pencolor("Blue")
    t.fd(300)
    t.right(90)
    x = x + 1
ts.exitonclick()