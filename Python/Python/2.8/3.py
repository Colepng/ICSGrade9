boxes = [0]
boxes.append(int(input("How many chocolate chip cookies do you want ")))
boxes.append(int(input("How many raisin cookies do you want ")))
boxes.append(int(input("How many shortbread cookies do you want ")))
boxes.remove(0)

if boxes[0] > 5 or boxes[1] > 5 or boxes[2] > 5 or sum(boxes) > 10:
    discount = 0.10
else:
    discount = 0

HST = 1.13

total = HST * (6.95 * sum(boxes) - (sum(boxes) * discount))
print(f"${total}")