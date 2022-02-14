# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
while True:
    index = word.find(char)
    if (len(word[index:]) < 3):
        break
    if (char in word and index < len(word)-2):
        print(word[index:index+3])
        word = word[index+1:]