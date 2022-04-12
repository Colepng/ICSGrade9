user_salary = int(input("What is your annual salary? "))
house_price = int(input("What is the price of the house? "))
if_deposit = input("Do you have a deposit to put towards the house? ")

if if_deposit.lower() == "yes":
    user_deposit = True
else:
    user_deposit = False

mortgage = user_salary * 4

if mortgage > house_price and user_deposit == True:
    print("You can afford the house and you have a deposit")
elif mortgage > house_price and user_deposit == False:
    print("You can afford the house but you don't have a deposit")
elif mortgage < house_price and user_deposit == True:
    print("You can't afford the house but you have a deposit")
elif mortgage < house_price and user_deposit == False:
    print("You can't afford the house and you don't have a deposit")


