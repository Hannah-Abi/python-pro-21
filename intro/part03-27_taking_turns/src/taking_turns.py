# Write your solution here
num = int(input("Please type in a number: "))
i = 1
while i <= num/2:
    print(i)
    print(num-i+1)
    i += 1
if (num%2 == 1):
    print(int((num +1)/2))