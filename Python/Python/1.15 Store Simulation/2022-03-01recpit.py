print("\t\t\t Welcome To Fred's Food")
x = int(input("\t How many differnt items do you have on the receipt "))
loop1 = 0
items = [0]
while(loop1<x):
    items_info = (input("Please Input the name of your items, then the amount and the individual price with no dollor sign ").split())
    items.append(items_info)
    loop1 = loop1 + 1
items.remove(0)
print("array:", items)    
#take multiple inputs in array




##all_items = [0]
##print(*all_items, sep = "\n")
##sum_of_items = sum(all_items)
##print("Total of all items:",sum_of_items)
##tax = sum_of_items*0.13
##tip = tax*0.15
##print("Tax:",tax)
##print("15% tip:",tip)
##total = sum_of_items + tax + tip
##print("Total:",total)


