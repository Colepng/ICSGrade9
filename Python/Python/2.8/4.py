int1 = int(input("Please input an integer "))
int2 = int(input("Please input an integer "))
int3 = int(input("Please input an integer "))

def multiple():
    if int1%int2 == 0 or int1%int3 == 0 or int2%int1 == 0 or int2%int3 == 0 or int3%int2 == 0 or int3%int1 == 0 :
        print("One or more integers is a mutiple of one of the others")
    else:
        print("None of the integers is a mutiple of one of the others")

def great():
    if int1 > 10 and int2 > 10 and not int3 > 10:
        print("int1 and int2 is grater then 10 and not int3")
    elif int1 > 10 and int3 > 10 and not int2 > 10:
        print("int1 and int3 is grater then 10 and not int2")
    elif int2 > 10 and int3 > 10 and not int1 > 10:
        print("int2 and int3 is grater then 10 and not int1")
    else:
        print("2 integers or more integers are not greater than 10")

multiple()
great()