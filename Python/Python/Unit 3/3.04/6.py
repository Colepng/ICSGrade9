start_value = abs(int(input("Please enter the value to start at ")))
end_value = abs(int(input("Please enter the value to end at "))) + 1
counter = abs(int(input("Please enter the value to count by ")))
for i in range(start_value, end_value, counter):
    print(f"The loop has run {i} times.")