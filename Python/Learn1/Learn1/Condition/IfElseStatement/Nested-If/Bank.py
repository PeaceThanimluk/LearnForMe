#Nested-If
Username = input("Username : ")
Password = input("Password : ")
LogIn = False

if Username == "Member" and Password == "1234" and LogIn == False:
    LogIn = True

    if LogIn == True:
        print("Login succes!")
        Service = input("Choose your service(1-2) : ")

        if Service == "1":
            print("Withdraw")
        elif Service == "2":
            print("Deposit")
        else:
            print("Invalid! , Please try again!")
else:
    print("User not found!")