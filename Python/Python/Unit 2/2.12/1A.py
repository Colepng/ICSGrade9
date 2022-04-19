num1 = 7
num2 = 2
num3 = 7
if num1 == num2:
    if num1 == num3:
        print("All numbers are the same")
    else:
        print("num1 and num2 have the same values")

else:    
    if num2 == num3:
        
        if num1 == num3:
            print("All numbers are the same")
            
        else:
            print("num2 and num3 have the same values")
            
    if num1 < num2:
        if num1 < num3:
            print("Num 1 is the smallest")
        else:
            print("Num 3 is the smallest")
    else:
        if num2 < num3:
            print("Num 2 is the smallest")
        else:
            print("Num 3 is the smallest")
