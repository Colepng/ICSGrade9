name = input("What is your name? ")

print(f"Hello {name} its lovely to meet you")

loop = "yes"
while loop == "yes" or loop =="Yes":
    ran = False
    feeling = input("How are you today? my supported feelings are currently Excited, Happy, Ok and Tired ")
    if feeling == "Excited":
        print("Fantastic. What are you feeling excited about?")
    elif feeling == "Happy":
        print("I am happy too. Yay")
    elif feeling == "Ok":
        print("How can I cheer you up?")
    elif feeling == "Tired":
        print("Get some rest?")
    else:
        loop = input("You didn't enter a supported feeling would you like to enter a differnt one ")
        ran = True
    if ran == False: loop = input("Would you like to enter a differnt feeling ")
    
