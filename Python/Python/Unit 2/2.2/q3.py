MASTER_PASSWORD = "PASSWORD"

try_again = True

while try_again:
    user_pass = input("Please input your password ")
    if MASTER_PASSWORD == user_pass:
        print("Password Accepted")
        try_again = False
    else:
        again = input("Would you like to try again, Input yes if you would like to or no if you would like to stop ")
        if again == "no":
            try_again = False