# Write your solution here
number = int(input("Number: "))
if (number%5 == 0 and number%3 != 0):
    print("Buzz")
if (number%5 != 0 and number%3 == 0):
    print("Fizz")
if (number%5 == 0 and number%3 == 0):
    print("FizzBuzz")
