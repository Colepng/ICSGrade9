name = input('What is your name ')
is_dr = input('Are you a doctor ')

if is_dr.lower() == 'yes':
    print(f'Dr.{name}')

else:
    gender = input('Are you male, female or other. If other please input what you want your title to be ')
    
    if gender.lower() == 'male':
        print(f'Mr.{name}')
    else:
        if gender.lower() == 'female':
            print(f'Ms.{name}')
        else:
            print(f'{gender}.{name}')