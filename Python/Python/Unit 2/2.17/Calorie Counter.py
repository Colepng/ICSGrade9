
#prints outs a part of the menu and ask the user for what they want from there
print("Welcome to El Chip's")

print("Here are three main choices")

print("")
print('1 - 2 slices of a 14" pizza (570 Calories)')
print("2 - 6 oz Hambuger (502 Calories)")
print("3 - Pasta (300 grams)(393 Calories)")
print("4 - None")
print("")

main_choice = int(input("Please enter a main choice "))

print("Here are three side choices")

print("")
print("1 - Caesar Salad (102 grams)(160 calories)")
print("2 - Medium french fries (117 grams)(312 calories)")
print("3 - 3 slices of garlic bread (618 Calories)")
print("4 - None")
print("")

side_choice = int(input("Please enter a side choice "))

print("Here are three drink choices")

print("")
print("1 - Carbonated drink (21 fl. oz)(182 Calories)")
print("2 - Fresh squised orange juice (21 fl. oz)(294 Calories)")
print("3 - Water (0 Calories)")
print("4 - None")
print("")

drink_choice = int(input("Please enter a drink choice "))

print("Here are three dessert choices")

print("")
print("1 - 1 piece of Angel food cake (50 grams)(129 Calories)")
print("2 - Vanilla ice cream (66 grams)(127 Calories)")
print("3 - Lava cake (75 grams)(270 Calories)")
print("4 - None")
print("")

dessert_choice = int(input("Please enter a dessert choice "))

total_calories = 0


#adds calories to the total count based of what the user chose
if main_choice == 1:
    total_calories += 570

elif main_choice == 2:
    total_calories += 502

elif main_choice == 3:
    total_calories += 393



if side_choice == 1:
    total_calories += 160

elif side_choice == 2:
    total_calories += 312

elif side_choice == 3:
    total_calories += 618



if drink_choice == 1:
    total_calories += 182

elif drink_choice == 2:
    total_calories += 294

elif drink_choice == 3:
    total_calories += 0



if dessert_choice == 1:
    total_calories += 129

elif dessert_choice == 2:
    total_calories += 127

elif dessert_choice == 3:
    total_calories += 270

#pritns out the total calorie count
print(f'Your total calorie count is {total_calories}')