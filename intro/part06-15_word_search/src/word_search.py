# Write your solution here
import re
def find_words(search_term: str):
    dict = []
    with open("words.txt") as word_file:
        for line in word_file:
            dict.append(line.strip())
    word_list = []
    star = "*"
    dot = "."
    if dot in search_term:
        for value in dict:
            if re.search(search_term, value) and len(search_term) == len(value):
                word_list.append(value)
    if star in search_term:
        term = search_term.replace(star, "")
        if star == search_term[0]:
            for value in dict:
                if value.endswith(term):
                    word_list.append(value)
        if star == search_term[-1]:
            for value in dict:
                if value.startswith(term):
                    word_list.append(value)
    if star not in search_term and dot not in search_term:
        for value in dict:
            if value == search_term:
                word_list.append(value)
    
    return word_list

if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("p.ng"))
    print(find_words(".a.e"))
    print(find_words("hello"))
    print(find_words("reson*"))
    