# Write your solution here
name = input("Please tell me your name: ")
if name == "Jerry":
    print("Next please!")
if name != "Jerry":
    portion = int(input("How many portions of soup? "))
    print(f"The total cost is {portion*5.9}")
    print("Next please!")