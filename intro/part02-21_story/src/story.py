# Write your solution here
code = ""
attemp = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == attemp:
        print(code)
        break
    else:
        code += word + " "
        attemp = word
