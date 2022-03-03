import turtle as t
ts = t.Screen
t.pencolor("Red")
t.pensize(5)
t.fillcolor("Orange")
t.begin_fill()
z = 0
while(z<2):
    t.fd(190)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    z = z + 1
t.end_fill()
t.exitonclick()