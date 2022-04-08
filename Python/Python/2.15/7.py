password = input("Please enter a password between 6-12 characters")
passlen = len(password)

if passlen >= 6 and passlen <= 12:
    print("Password accepted")
else:
    print("Password invaild")