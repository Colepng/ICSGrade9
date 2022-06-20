import random
 
print("""Hello user you are playing a guessing game
This game will stop when you guess the correct number between 1-100
You will be asked to input a number depending on what that number is you will receive a hint""")
 
random_number = random.randint(1, 100)
print(random_number)
guess = 0
while guess != random_number: #Checks if the guess is not equal to the random number
    guess = int(input("Please input your guess "))
    
 
    if guess > random_number:#Prints a hint depending if the guess is less then or greater then the random number
        print("Too high")
    elif guess < random_number:
        print("Too low")
 
print("Congrats you guessed the right number")