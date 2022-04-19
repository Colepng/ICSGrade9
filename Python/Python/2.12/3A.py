price = int(input('What is the price of the tv? '))
size = int(input('How big is the tv? '))
tv_model = input('Are you buying a plasma tv or LCD? ')

if tv_model.lower() == 'plasma':
    discounted_price = price - price * 0.05
    print(f'The discounted price is ${discounted_price}')
elif tv_model.upper() == 'LCD':
    if size == 30:
        discounted_price = price - price * 0.08
        print(f'The discounted price is ${discounted_price}')
    elif size == 42:
        discounted_price = price - price * 0.10
        print(f'The discounted price is ${discounted_price}')
    else:
        print(f'The price is ${price}')