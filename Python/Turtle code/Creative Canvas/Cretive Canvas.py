import turtle as t
ts = t.Screen()         #stating varibles
x = 0       
ts.bgcolor("black")     #stating colours
t.colormode(255)
t.pencolor(25, 208, 248)
t.fillcolor(25, 208, 248)
print("What coordinates would you like the middle to be, please put the x coordinates frist then y")
start_x = int(input())              #starting position 
start_y = int(input())
t.penup()
t.goto(start_x, start_y)               
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(150)
t.lt(65)
t.fd(100)
t.lt(50)
t.pendown()
t.begin_fill()
while (x<9):
    t.begin_fill()      #Loop to  make shape
    t.circle(225, 35)
    t.lt(135)
    t.fd(194)
    t.lt(140)
    t.fd(96)
    t.lt(50)
    t.circle(225, 35)
    t.end_fill()
    t.penup()
    t.circle(225, 5)
    t.pendown()
    x = x + 1
t.exitonclick()