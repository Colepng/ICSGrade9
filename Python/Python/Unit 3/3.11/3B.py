total = 0

for die1 in range(1,7):
    for die2 in range(1,7):
        for die3 in range(1,7):
            die1_die2_die3 = die1 + die2 + die3
            if die1_die2_die3 < 12 and die1_die2_die3 > 7 and die1_die2_die3 < 11:
                
                for i in range(2,die1_die2_die3):
                    if die1_die2_die3 % i == 0:
                        break

                else:
                    # print(die1_die2_die3)
                    # print(i,"times",die1_die2_die3//i,"is",die1_die2_die3)
                    # print("True")
                    total += 1

print("There are", total, "possible rolls that sum are less then 12, between 7 and 11 and a prime number")