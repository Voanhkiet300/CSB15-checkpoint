# bai 1:

# print("== Registration ==")
# username = input("Username: ")
# password = input("Password: ")
# email = input("Email: ")
# print("Registered successfully.")

# bai 2:

# print("== Registration ==")
# username = input("Username: ")
# password = input("Password: ")
# repeatPassword = input("Repeat Password: ")
# while   password != repeatPassword:
#     print("Passwords do not match. Please input again.")
#     repeatPassword = input("Repeat Password: ")
#     continue
# email = input("Email: ")
# print("Registered successfully.")

# bai 3:

print("== Registration ==")
username = input("Username: ")

password = input("Password: ")
while len(password) < 8 or password.isalpha() or password.isdigit():
    print("Invalid password. Please input again.")
    password = input("Password: ")
    continue

repeatPassword = input("Repeat Password: ")
while password != repeatPassword:
    print("Passwords do not match. Please input again.")
    repeatPassword = input("Repeat Password: ")
    continue

email = input("Email: ")
while email.find("@") == -1 or email.find("@")+1 == len(email) or email.find(".") == -1 or email.find(".")+1 == len(email):
    print("Invalid email. Please input again.")
    email = input("Email: ")
    continue
print("Registered successfully.")

