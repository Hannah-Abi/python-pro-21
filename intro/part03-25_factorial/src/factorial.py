# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if (number <= 0):
        print("Thanks and bye!")
        break
    i = 1
    f = 1
    while i <= number:
        f = f*i
        i += 1
    print(f"The factorial of the number {number} is {f}")
