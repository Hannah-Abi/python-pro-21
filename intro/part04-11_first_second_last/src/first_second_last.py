# Write your solution here
def first_word(word):
    sp = word.find(" ")
    return word[:sp]
def second_word(word):
    i = 0
    while True:
        sp = word.find(" ")
        if (i == 1):
            if (sp == -1):
                return word
            else:
                return word[:sp]
            break
        word = word[sp+1:]
        i += 1
def last_word(word):
    i = 0
    while True:
        sp = word.find(" ")
        if (sp == -1):
            return word
            break
        word = word[sp+1:]
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))