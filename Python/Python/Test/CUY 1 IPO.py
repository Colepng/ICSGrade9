#classes
import math

#Creating variables
x1 = float(input("Please input your x1 point"))
y1 = float(input("Please input your y1 point"))
x2 = float(input("Please input your x2 point"))
y2 = float(input("Please input your y2 point"))

#Does the formula to find the distance of two points and puts the valve in to the variable distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Outputting the distance
print("The distance between point x1,y1 and x2.y2 is", distance)

