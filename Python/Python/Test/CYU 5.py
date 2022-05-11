# #Question 1
# total = 0
# print("Numbers between 100 and 200, divisble by 9:")
# for i in range(100,201):
#     if i%9 == 0:#checks if divisble by 9
#         total += i
#         print(i, end=" ")#outputs number divisble by 9
# print()
# print(f"The sum: {total}")#outputs sum



#Question 2
cost = []
for i in range(0,9):
    cost.append(int(input("Please input a integer ")))#gets 9 integers from the user
num_of_even = 0
largest_even = 0
total_of_even = 0
for x in range(len(cost)):
    if cost[x]%2 == 0:#Checks if its a even number
        num_of_even += 1#adds one
        total_of_even += cost[x]
        if largest_even < cost[x]:#If the number is larger than the old number replace it with the new number
            largest_even = cost[x]
        # print(cost[x], num_of_even, total_of_even, largest_even)
avg_of_even = total_of_even/num_of_even#Calculate avg
#Outputs the info we found
print(f"There is {num_of_even} even numbers")
print(f"The avg of the even numbers is {avg_of_even}")
print(f"The largest even number is {largest_even}")