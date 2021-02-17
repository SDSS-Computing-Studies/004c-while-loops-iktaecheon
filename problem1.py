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
username = input("str ")
password = input("str ")
count = 0
while username != "admin" and password != "12345":
    print("Access denied")
    count += 1
    if count > 3:
        break
    username = input("str ")
    password = input("str ")
if username == "admin" and password == "12345":
    print("Access granted")