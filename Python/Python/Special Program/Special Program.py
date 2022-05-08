from tkinter import *
from tkinter import messagebox
import turtle as t
import time

title = "Mother's day"
#time.sleep(2)
if messagebox.askquestion(title, "Would you like to see a heart") == 'yes':
    print("yes")
    t.fillcolor('red')
    t.begin_fill()
    t.left(45)
    time.sleep(2)
    t.fd(100)
    t.circle(50,180)
    t.right(90)
    t.circle(50,180)
    t.fd(100)
    t.end_fill()
    t.penup()
    t.goto(-50,100)
    t.write("Happy Mother's Day", True)
    t.exitonclick()

else:
    print("No")
    messagebox.showinfo(title,"Ok have a good day")




# messagebox.askokcancel()
# messagebox.askretrycancel()
# messagebox.askyesno()
# messagebox.askyesnocancel()
