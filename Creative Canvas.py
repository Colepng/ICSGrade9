import turtle as t
import random as r
ts = t.Screen()
ts.setup(800, 800)
t.ht()
loop = 0
x = 0
t.colormode(255)
t.pencolor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
ts.bgcolor("black")
shapes = ["triangle", "square", "pentagon", "hexagon", "septagon", "octagon"]
print("Chose a shape from this list, and input your selction")
for i in shapes:
    print(i, end = ' ')
print("")
user_shape = input()
if(user_shape == shapes[0]):
    print("triangle")
    while(x<3):
            t.fd(100)
            t.lt(120)
            x = x + 1   
elif(user_shape == shapes[1]):
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
elif(user_shape == shapes[2]):
    print("pentagon")
    while(x<5):
        t.fd(100)
        t.lt(72)
        x = x + 1   
elif(user_shape == shapes[3]):
    print("hexagon")
    while(x<6):
        t.fd(100)
        t.lt(60)
        x = x + 1   
elif(user_shape == shapes[4]):
    print("septagon")
    while(x<7):
        t.fd(100)
        t.lt(51.429)
        x = x + 1
    
elif(user_shape == shapes[5]):
    print("octagon")
    while(x<8):
        t.fd(100)
        t.lt(45)
        x = x + 1
t.exitonclick()
