# Write your solution here
attemp = 0
while True:
    pin = int(input("PIN: "))
    attemp += 1
    if (pin == 4321 and attemp == 1):
        print("Correct! It only took you one single attempt!")
        break
    if (pin != 4321):
        print("Wrong")
    if (pin == 4321 and attemp != 1):
        print(f"Correct! It took you {attemp} attempts")
        break