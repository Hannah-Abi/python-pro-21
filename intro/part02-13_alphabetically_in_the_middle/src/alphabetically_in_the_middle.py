# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3st letter: ")
if (first < second): 
    if (third > second):
        print(f"The letter in the middle is {second}")
    elif (third < first):
        print(f"The letter in the middle is {first}")
    elif (first< third < second):
        print(f"The letter in the middle is {third}")
else:
    if (third < second):
        print(f"The letter in the middle is {second}")
    elif (third > first):
        print(f"The letter in the middle is {first}")
    elif (second<third<first):
        print(f"The letter in the middle is {third}")