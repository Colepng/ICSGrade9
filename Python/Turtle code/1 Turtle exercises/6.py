import turtle as t
ts = t.Screen()
t.lt(90)
t.fillcolor("Brown")
t.begin_fill()
s = 0
d = 0
w = 0
w2 = 0
while (s<4):
    t.fd(150)
    t.lt(90)
    s = s + 1
t.end_fill()
t.lt(90)
t.fd(50)
t.rt(90)
t.fillcolor("Blue")
t.begin_fill()
while (d<3):
    t.fd(50)
    t.lt(90)
    d = d + 1
t.end_fill()
t.fillcolor("red")
t.lt(180)
t.fd(50)
t.rt(90)
t.fd(150)
t.begin_fill()
t.rt(45)
t.fd(106)
t.rt(90)
t.fd(106)
t.end_fill()
t.rt(45)
t.fd(40)
t.rt(90)
t.penup()
t.fd(65)
t.pendown()
t.fillcolor("White")
t.begin_fill()
while (w<4):
    t.lt(90)
    t.fd(40)
    w = w + 1
t.penup()
t.fd(20)
t.pendown()
while (w2<4):
    t.fd(40)
    t.lt(90)
    w2 = w2 + 1
t.end_fill()
t.penup()
t.lt(180)
t.fd(85)
t.pendown()
t.fillcolor("Yellow")
t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(110)
t.rt(90)
t.fd(100)
t.end_fill()
t.exitonclick()