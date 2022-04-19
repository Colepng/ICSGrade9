day = int(input("Please input the day of the month "))

month = int(input("Please input the month as a number "))

if day == 25 and month == 12:
    print("Hooray! It’s Christmas Day!")

elif day < 25 and month == 12:
        print("Christmas is just around the corner!")

else:
    print("You’ve still got a while to go until Christmas.")