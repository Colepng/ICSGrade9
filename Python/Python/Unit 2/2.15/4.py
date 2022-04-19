username = input("What is your username? ")

if username == "rob-bot":
    password = input("What is your password ")
    if password == "ilovepython":
        print("Access granted. Have a lovely day!")
    else:
        print("Intruder alert!")
else:
    print("Intruder alert")