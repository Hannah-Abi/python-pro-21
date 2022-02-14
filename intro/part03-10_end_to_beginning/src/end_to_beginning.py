# Write your solution here
str = input("Please type in a string: ")
count = 0
while count< len(str):
    print(str[len(str) - count-1])
    count += 1