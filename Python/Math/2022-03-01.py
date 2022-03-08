x = int(input("How many item do you have on the receipt"))
loop1 = 0
all_items = [0]
while(loop1<x):
    item_cost = float(input("What is the price of one of item"))
    all_items.append(item_cost)
    loop1 = loop1 + 1
all_items.remove(0)
print(*all_items, sep = "\n")
sum_of_items = sum(all_items)
print("Total of all items:",sum_of_items)
tax = sum_of_items*0.13
tip = tax*0.15
print("Tax:",tax)
print("15% tip:",tip)
total = sum_of_items + tax + tip
print("Total:",total)


