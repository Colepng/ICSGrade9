age = int(input("What is your age "))
if age <= 0: print("Invaild age")
    
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teen")
elif age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
