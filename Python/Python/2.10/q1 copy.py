x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))


if (x >= y) and (x >= z):  # x is biggest
   print("x is the biggest")
elif (y >= z): 		# x isn't biggest
   print("y is the biggest")
else: 			# x, y not biggest
   print("z is the biggest")