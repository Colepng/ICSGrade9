total = 0

for die1 in range(1,7):
    for die2 in range(1,7):
        die1_die2 = die1 + die2
        if die1_die2 > 8 and not die1_die2 % 3 == 0 and not die1_die2 % 5 == 0:
            total += 1
            #print(die1, die2)
print("There are", total, "possible rolls that sum are at least 9 and not divisible by 3 or 5.")