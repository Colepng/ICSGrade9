#variables
milk_price = 1
eggs_price = 1.5
juice_price = 2
plums_price = 1.30
cucum_price = 0.5
tubs_price = 2.5
HST = 0.13
print("\t\t\t Welcome To Fred's Food:")
print()
print("Enter the amount of each thing you would like to buy.")
print()
milk = int(input("1. How many bags of milk would you like? "))
eggs = int(input("2. How many cartons of eggs would you like? "))
juice = int(input("3. How many cartons of juice would you like? "))
plums = int(input("4. How many plums would you like? "))
cucum = int(input("5. How many cucumbers would you like? "))
tubs = int(input("6. How many tubs of ice cream would you like? "))
#finding the total amount
milk_sum = milk * milk_price
eggs_sum = eggs * eggs_price
juice_sum = juice * juice_price
plums_sum = plums * plums_price
cucum_sum = cucum * cucum_price
tubs_sum = tubs * tubs_price
sub_total = milk_sum + eggs_sum + juice_sum + plums_sum + cucum_sum + tubs_sum
tax = sub_total * HST
total = sub_total + tax
print("\t\t\t Your Bill")
print(milk, "Milk @ $" + str(milk_price),"=", milk_sum)
print(eggs, "Milk @ $" + str(eggs_price),"=", eggs_sum)
print(juice, "Milk @ $" + str(juice_price),"=", juice_sum)
print(plums, "Milk @ $" + str(plums_price),"=", plums_sum)
print(cucum, "Milk @ $" + str(cucum_price),"=", cucum_sum)
print(tubs, "Milk @ $" + str(tubs_price),"=", tubs_sum)
print()
print("Subtotal: $" + str(sub_total))
print("tax: $" + str(tax))
print("Total: $" + str(total))

