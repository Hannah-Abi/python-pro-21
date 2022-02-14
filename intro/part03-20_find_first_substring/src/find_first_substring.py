# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)
if (char in word and index < len(word)-2):
    print(word[index:index+3])