# write your solution here
sentence = input("Write text: ")
check_list = []
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
print(text)