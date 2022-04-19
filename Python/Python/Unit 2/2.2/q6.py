price = float(input("Enter the price for your meal "))

HST = 0.13
total_tax = 0
if price > 4.00:
    total_tax = price*0.13

total = price + total_tax

print(f"Subtotal: ${price}")
print(f"Total tax: ${total_tax}")
print(f"Total: ${total}")