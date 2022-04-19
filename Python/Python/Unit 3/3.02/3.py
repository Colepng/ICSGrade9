numbers = []
for i in range(5):
    numbers.append(int(input('Please input a number')))
num_remove = numbers.index(int(input('Please chose one number to remove')))
numbers.pop(num_remove)
print(f'Your list{numbers}')
print(f'The length of your list is {len(numbers)}')
print(f'The sum of your list is {sum(numbers)}')
