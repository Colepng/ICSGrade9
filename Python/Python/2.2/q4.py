
line_count = int(input("Please input your line count "))
page_count = int(input("Please input your page count "))
page_length = int(input("Please input your page length "))



loop = True
while loop:
    if line_count > page_length:
        page_count += 1
        line_count -= page_length
    else:
        loop = False
print(f"Your new page count is {page_count}")