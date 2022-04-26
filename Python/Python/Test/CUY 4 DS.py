#loops untill the total amount of cupcakes is greater than or equal to 28
while 1:
    reg_box = int(input("How many regular boxes do you have? "))
 
    #loops untill the user inputs a number above 0
    while 1:
        if reg_box > 0:
            break#breaks the loop
 
        else:
            reg_box = int(input("How many regular boxes do you have? Make sure your number is greater than 0. ")) 
 
 
 
 
    small_box = int(input("How many small boxes do you have? "))
 
    #loops untill the user inputs a number above 0
    while 1:
        if small_box > 0:
            break#breaks the loop
 
        else:
            small_box = int(input("How many small boxes do you have? Make sure your number is greater than 0. "))
 
 
    #calculates the total amount of cupcakes
    cupcake_reg = reg_box * 8
    cupcake_small = small_box * 3
    cupcake_total = cupcake_reg + cupcake_small
    #check is the total amount of cupcakes is greater or equal to 28 and is so breaks the loop
    if cupcake_total >= 28: 
        break
    else:
        print("Please input a minimum of 28 cupcakes total")
print(f"You have {cupcake_total} cupcakes")