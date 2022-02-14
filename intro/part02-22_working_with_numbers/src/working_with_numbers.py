# Write your solution here
count = 0
sum = 0
povcount = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    else:
        count += 1
        sum += number
        if (number > 0):
            povcount += 1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/count}")
print(f"Positive numbers {povcount}")
print(f"Negative numbers {count-povcount}")

