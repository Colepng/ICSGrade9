weekly_sale = int(input("Please input weekly sales "))

if weekly_sale > 1000:
    bonus = weekly_sale * 0.05
    print(f"The bonus earned on ${weekly_sale} worth of sales is ${bonus}")
else: print("You did not earn a bonus")