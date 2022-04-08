amount_of_widgets = int(input("How many widgets are you buying "))
cost_per_widget = int(input("What is the cost per widget "))

if amount_of_widgets < 0 and cost_per_widget < 0: print("Both input are invaild")
run = False
elif amount_of_widgets < 0:
    print("Invaild amount of widgets") run = False
elif cost_per_widget < 0:
    print("Invaild cost per widget") run = False                                                   
discount = 0


while run:
    sum_of_widget = round(amount_of_widgets * cost_per_widget, 2)

    if amount_of_widgets > 325 or sum_of_widget > 1000:
        discount = 0.15

    HST = 0.13


    dis_widget = round(sum_of_widget * discount, 2)
    after_discount = sum_of_widget - dis_widget
    tax = round(after_discount * HST, 2)
    final_cost = round(after_discount + tax, 2)

    print(f"Before discount\t${sum_of_widget}")
    if discount == 5:
        print(f"After discount\t${after_discount}")
        print(f"You saved\t${dis_widget}")
    print(f"Tax\t\t${tax}")
    print(f"Total\t\t${final_cost}")
