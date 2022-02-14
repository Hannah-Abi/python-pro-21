# Write your solution here
number = int(input("Please type in a number: "))
i = 1
t = 1
while i <= number:
    for t in range(1, number + 1):
        print(f"{i} x {t} = {t*i}") 
    i += 1