import turtle as t
ts = t.Screen
t.pencolor("Purple")
t.pensize(5)
t.fillcolor("Blue")
t.begin_fill()
z = 0
while(z<4):
    t.fd(180)
    t.rt(90)
    z = z + 1
t.end_fill()
t.exitonclick()