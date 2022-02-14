# Write your solution here
import random
def words(n: int, beginning: str):
    dict = []
    with open("words.txt") as dict_file:
        word_list = []
        for line in dict_file:
            line = line.strip()
            if line.startswith(beginning):
                word_list.append(line)
        #rase ValueError exception if there are not enough words beginning with the specified string
        if len(word_list) < n:
            raise ValueError(f"The number of words required ({n}) is out of range")
        while len(dict) < n:
            random_word = random.choice(word_list)
            if random_word not in dict:
                dict.append(random_word)
    return dict

if __name__=="__main__":
    word_list = words(4, 'abs')
    for word in word_list:
        print(word)
