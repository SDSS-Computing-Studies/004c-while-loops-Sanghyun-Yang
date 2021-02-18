#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username = str(input()).strip()
password = str().strip()
while username != "admin":
    username = input().strip()
while username == "admin":
    while password != "12345":
        password = str(input()).strip()
        if password == "12345":
            print("Access granted")
            break
