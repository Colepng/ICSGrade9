import shutil
columns = shutil.get_terminal_size().columns

for i in range(0,3):
    output = -1
    for i in range(0,2+i):
        output += 2
        print(("*"*output).center(columns))