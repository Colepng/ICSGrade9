num4 = int(input("Please enter a positive 4-digit number(1000-9999)"))
digit1000 = num4//1000
num4_r = num4%1000
digit100s = num4_r//100
digit100_r = num4_r%100
digit10s = digit100_r//10
digit10_r = digit100_r%10
digit1_r = digit10_r//1
print("The digits of", num4, "are", digit1000, digit100s, digit10s, digit1_r)
            
