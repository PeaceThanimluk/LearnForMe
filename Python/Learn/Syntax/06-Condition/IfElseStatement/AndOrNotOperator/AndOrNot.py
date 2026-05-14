username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Succeed")
elif username != "admin" and password != "1234":
    print("Username and Password are not correct!")
elif username != "admin":
    print("Username is not correct!")
else:
    print("Password is not correct!")
