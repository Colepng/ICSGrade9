int1 = int(input('Please input a integer '))
int2 = int(input('Please input a integer '))


if int1 > 0 and int2 > 0:
    print('Both integers are positive')

elif int1 < 0 and int2 < 0:
    print('Both integers are negative')

else:
    print('One integer is positive and one is negative')