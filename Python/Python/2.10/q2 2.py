temp = int(input("Please input the temperature "))
max_temp = int(input("What is the max tempreature "))
min_temp = int(input("What is the minimum tempreature "))


if temp > min_temp: 
    if temp > max_temp: print("food is too hot")

    else: print("The food is a good temperature")

else:
    print("The food is too cold")