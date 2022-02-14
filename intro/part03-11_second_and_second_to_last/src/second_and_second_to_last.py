# Write your solution here
str = input("Please type in a string: ")
if (str[1] == str[len(str)-2]):
    print(f"The second and the second to last characters are {str[1]}")
else:
    print("The second and the second to last characters are different")