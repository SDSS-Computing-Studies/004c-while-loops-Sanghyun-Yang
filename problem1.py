##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
username = str(input())
password = str()
trying1 = int()
trying2 = int()
while username != "admin":
    username = str(input())
    trying = trying1 + 1
    if trying1 == 3:
        break
while username == "admin":
    while password != "12345":
        password = str(input())
        trying2 = trying2 + 1
        if trying == 3:
            break
        if password == "12345":
            print("Access granted")