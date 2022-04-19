year = int(input("Please enter a year "))

if year%4 == 0:
    if not year%100 == 0:
        print(f"{year} is a leap year ")
    else:
        if year%100 == 0 and year%400 == 0:
            print(f"{year} is a leap year ")

        else:
            print(f"{year} is not a leap year ")
else:
    print(f"{year} is not a leap year ")