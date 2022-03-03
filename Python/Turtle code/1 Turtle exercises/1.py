import turtle as t
ts = t.Screen
t.pencolor("Red")
t.fillcolor("Brown")
t.begin_fill()
z = 0
while(z<4):
    t.fd(100)
    t.rt(90)
    z = z + 1
t.end_fill()
t.exitonclick()