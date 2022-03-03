import turtle as t
ts = t.Screen()
s = 0
s2 = 0
while (s<3):
    t.fd(50)
    t.lt(90)
    s = s + 1
t.penup()
t.fd(100)
t.pendown()
while (s2<3):
    t.fd(50)
    t.lt(90)
    s2 = s2 + 1
t.exitonclick()