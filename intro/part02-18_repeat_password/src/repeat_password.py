# Write your solution here
pw = input("Password: ")
while True:
    repass = input("Repeat password: ")
    if (repass == pw):
        print("User account created!")
        break
    else:
        print("They do not match!")