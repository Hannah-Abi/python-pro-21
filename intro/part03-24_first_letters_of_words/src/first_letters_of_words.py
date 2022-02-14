# Write your solution here
sen = input("Please type in a sentence: ")
print(sen[0])
while True:
    index = sen.find(" ")
    if (index == -1):
        break
    print(sen[index+1])
    sen = sen[index +1:]
    