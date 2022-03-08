import turtle as t
loop1 = 0
x = 0
colour = [0]
colour.append(input("input a colour: "))
colour.append(input("input a colour: "))
colour.append(input("input a colour: "))
colour.append(input("input a colour: "))
colour.append(input("input a colour: "))
colour.append(input("input a colour: "))
colour.remove(0)
while(loop1<6):
    t.pencolor(colour[x])
    t.fd(100)
    t.lt(60)
    x = x + 1
    loop1 = loop1 + 1
t.exitonclick
