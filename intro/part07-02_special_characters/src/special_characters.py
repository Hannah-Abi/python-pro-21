# Write your solution here
import string
def separate_characters(my_string: str):
    ascii_ltr = ""
    punc_ltr = ""
    others = ""
    for i in my_string:
        if i in string.ascii_letters:
            ascii_ltr += i
        if i in string.punctuation:
            punc_ltr += i
        if i not in string.ascii_letters and i not in string.punctuation:
            others += i
    part = (ascii_ltr,punc_ltr,others)
    return part
if __name__=="__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
