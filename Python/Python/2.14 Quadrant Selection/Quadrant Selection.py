coord = [0]
coord.append(int(input("What is x ")))
coord.append(int(input("What is y ")))
coord.remove(0)

if (coord[0] < -1000 or coord[0] > 1000 )and (coord[1] < -1000 or coord[1] > 1000):
    print("Both of  your values are out of range")

elif coord[0] < -1000 or coord[0] > 1000:
    print("Your x value  is out of range")

elif coord[1] < -1000 or coord[1] > 1000:
    print("Your y value  is out of range")

else:
    if coord[0] > 0 and coord[1] > 0: #cheacks if both x and y are postive
        quad = "Q1"

    elif coord[0] < 0 and coord[1] < 0:#cheacks if both x and y are negtive
        quad = "Q3"

    elif coord[0] > 0 and coord[1] < 0:#checks if x is postive and if y is negitve 
        quad = "Q4"

    elif coord[0] < 0 and coord[1] > 0:#checks if x is negitve and if y is postive 
        quad = "Q2"

    elif coord[1] == 0 and coord[0] != 0:#checks if on the X axis
        quad = "X axis"

    elif coord[0] == 0 and coord[1] != 0:#checks if on the y axis
        quad = "Y axis"
    else:
        quad = "Orgin"
    print(quad)