import turtle as t
ts = t.Screen()
def right():
    t.seth(0)
def up():
    t.seth(90)
def left():
    t.seth(180)
def down():
    t.seth(270)
def turn_right():
    t.rt(10)
def turn_left():
    t.lt(10)
def foward():
    t.fd(50)
ts.onkeypress(right, "Right")
ts.onkeypress(up, "Up")
ts.onkeypress(left, "Left")
ts.onkeypress(down, "Down")
ts.onkeypress(turn_left, "a")
ts.onkeypress(turn_right, "d")
ts.onkeypress(foward, "w")
t.listen()
t.exitonclick()