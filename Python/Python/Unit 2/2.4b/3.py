hours = int(input("Please input your hours worked "))

if hours > 40:
    salary = 12*40 + 15*(hours-40)
else:
    salary = 12*hours
print(f"Your salary is ${salary}")