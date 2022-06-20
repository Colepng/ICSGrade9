import random
import time
 
print("""Hello user you are playing a guessing game
This game will stop when you guess the correct number between 2 numbers of your choice or when you run out of guess
You will be asked how many guesses you want if you want unlimeted then please input 0
You will be asked to input a number depending on what that number is you will receive a hint""")
max_guess = int(input("How many guesses would you like "))
while True:
    first_number, second_number = int(input("Your first number ")), int(input("Your second number "))
    #print(first_number, second_number)
    if first_number >= second_number:
        print("first_number can not be larger or euqal to your seconed number")
    else:
        break

random_number = random.randint(first_number, second_number)
#print(random_number)
guess = 0
guess_count = 0
start = time.perf_counter()
while guess != random_number: #Checks if the guess is not equal to the random number
    
    guess = int(input("Please input your guess "))

    guess_count += 1

    #print(max_guess, guess_count)
    if max_guess != 0 and max_guess < guess_count+1:
        print("You have reached you max amount of guesses")
        quit()
 
    if guess > random_number:#Prints a hint depending if the guess is less then or greater then the random number
        print("Too high")
    elif guess < random_number:
        print("Too low")

    
end = time.perf_counter()

print(f"Congrats you guessed the right number, With {guess_count} amount of guess and It took you {round(end-start, 2)} seconeds")