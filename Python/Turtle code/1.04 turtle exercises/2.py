import turtle as t
ts = t.Screen()
t.fillcolor("Green")
t.pencolor("Red")
t.begin_fill()
x = 0 
while(x<4):
    t.fd(90)
    t.right(90)
    x = x + 1  
t.end_fill()
ts.exitonclick()