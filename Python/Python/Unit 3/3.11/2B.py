for i in range(0,3):
    old_x = 0
    first_run = True
    for x in range(1,6):
        if first_run:
            output = x
            first_run = False
        elif x < 4:
            output += 2
        else:
            output -= 2
        # print(test, x)
        print("*"*output)