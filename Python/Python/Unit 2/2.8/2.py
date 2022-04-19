right_tire_front = int(input("Please input your right front tire pressure "))
left_tire_front = int(input("Please input your left front tire pressure "))
right_tire_back = int(input("Please input your right front tire pressure "))
left_tire_back = int(input("Please input your right front tire pressure "))

if right_tire_front == left_tire_front and right_tire_back == left_tire_back:
    print("Pressure in all wheels is good")
else:
    print("Pressure is bad")