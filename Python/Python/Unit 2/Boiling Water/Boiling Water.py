#gets the water boiling point
boiling_temp = float(input("Please enter a water boiling point in celsius "))


#checks if the entered temperature is outside of the acceptable range
if boiling_temp < 80 or boiling_temp > 200:
    print("You entered an unsupported temperature")
    
else:
    atmos_press = 5 * boiling_temp - 400
    if atmos_press > 100:
        sea_level = 1
    elif atmos_press <100:
        sea_level = -1
    else:
        sea_level = 0
    print(f"The atmospheric pressure is {atmos_press}kPa")
    print(f"We are at {sea_level}")
