# Write your solution here
import difflib
import keyword
sentence = input("Write text: ")
check_list = []
incorrect_words = []
with open("wordlist.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            check_list.append(line)
text = ""
word_list = sentence.split()
#print(word_list)
for word in word_list:
    lcs_word = word.lower()
    if lcs_word in check_list: 
        text += f" {word}"
    else:
        text += f" *{word}*"
        incorrect_words.append(lcs_word)
print(text)
print("suggestions:")
for word in incorrect_words:
    close_words = difflib.get_close_matches(word,check_list,3)
    print(f"{word}: {', '.join(close_words)}")
