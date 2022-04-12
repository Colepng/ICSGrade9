num1 = 6
num2 = 7
num3 = 2

if num1 == num2:
    if num1 == num3:
        all_num = True
    else:
        num1_2 = True
elif num2 == num3:
    num2_3 = True
elif num1 == num3:
    num1_3 = True

    
if not all_num:


    if not num1_2:
        if num1 > num2:
            if num1 > num3:
                print("Num 1 is the largest")
            else:
                print("Num 3 is the largest")
    else:
        if not num1_2:
            if num2 > num3:
                print("Num 2 is the largest")
            else:
                print("Num 3 is the largest")
        else:
            print("The smallest spot it tied with num1 and num2")
