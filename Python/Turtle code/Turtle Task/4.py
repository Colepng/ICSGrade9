import turtle as t
import random as ran
t.speed(10)
ts = t.Screen()
ts.colormode(255)
ts.bgcolor('black')
s = 0
r = ran.randint(0, 255)
g = ran.randint(0, 255)
b = ran.randint(0, 255)
rgb = [r,g,b]
r = ran.randint(0, 255)
g = ran.randint(0, 255)
b = ran.randint(0, 255)
rgb2 = [r,g,b]
r = ran.randint(0, 255)
g = ran.randint(0, 255)
b = ran.randint(0, 255)
rgb3 = [r,g,b]
colors = [rgb, rgb2, rgb3]
length = ran.randint(10, 100)
angle  = ran.randint(25,90) #above 120 will  make a cool pattern and 60 will make the lines line up
while (s<130): 
    t.pencolor(rgb)
    t.lt(angle)    
    t.fd(length)
    t.pencolor(rgb2)
    t.lt(angle)    
    t.fd(length) 
    t.pencolor(rgb3)
    t.lt(angle)    
    t.fd(length)      
    s = s + 1
    length = length + 10
t.exitonclick()