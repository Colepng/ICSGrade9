import shutil
columns = shutil.get_terminal_size().columns

num = int(input("Enter a number: "))
columns = shutil.get_terminal_size().columns
for i in range(0,3):
    go_down = False
    old_x = 0
    first_run = True
    output = 0
    for x in range(1,num+1):
        if output == num:
            go_down = True

        if first_run:
            output = x
            first_run = False

        elif go_down == True:
            output -= 2

        elif output < num:
            output += 2
        
        print(("*"*output).center(columns))
while 1:
    pass