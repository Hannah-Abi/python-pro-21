# Write your solution here
word = input("Please type in a string: ")
sub = input("Please type in a substring: ")
i = 0
count = 0
while True:
    index = word.find(sub)
    if (index == -1):
        print("The substring does not occur twice in the string.")
        break
    if (sub in word):
        word = word[len(sub)+index:]
        count += index
        i += 1
    if (i == 2):
        print(f"The second occurrence of the substring is at index {count+len(sub)}.")
        break