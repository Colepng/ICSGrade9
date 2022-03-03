import turtle as t
ts = t.Screen()
p = 0
h = 0
o = 0
d = 0
while (p<5):
    t.lt(72)
    t.fd(50)
    p = p + 1
t.penup()
t.lt(180)
t.fd(200)
t.pendown()
while (h<6):
    t.rt(60)
    t.fd(50)
    h = h + 1
t.penup()
t.fd(150)
t.pendown()
while (o<8):
    t.rt(45)
    t.fd(50)
    o = o + 1
t.penup()
t.lt(90)
t.fd(200)
t.pendown()
t.lt(90)
while (d<10):
    t.lt(36)
    t.fd(50)
    d = d + 1
t.exitonclick()