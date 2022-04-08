x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))


if (x >= y):      	# y isn't biggest
   if (x >= z):    	# y, z not biggest 
      print("x is the biggest")
   else: 	  	# y, x not biggest
      print("z is the biggest")
elif (y >= z):     	# x, z not biggest
   print("y is the biggest")
else: 			# x, y not biggest
   print("z is the biggest")