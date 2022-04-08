temp = int(input("Please input the temperature "))
max_temp = int(input("What is the max tempreature "))
min_temp = int(input("What is the minimum tempreature "))


if temp > max_temp: print("Food is too hot")

elif temp < min_temp: print("food is too cold")

elif temp <= max_temp and temp >= min_temp: print("The food is a good temperature")