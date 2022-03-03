import turtle as t
ts = t.Screen()
ts.screensize()
ts.setup(800, 800)
t.ht()
t.penup()
t.goto(-398,398)
t.pendown()
while(loop<4):
    t.fd(200)
    t.rt(90)
    loop = loop + 1
loop=0
t.rt(90)
t.fd(400)
while(loop<2):
    t.lt(90)
    t.fd(200)
    loop = loop + 1
loop=0
t.lt(180)
t.fd(200)
while(loop<3):
    t.lt(90)
    t.fd(200)
    loop = loop + 1
loop=0
while(loop<3):
    t.rt(90)
    t.fd(200)
    loop = loop + 1
