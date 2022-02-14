# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    substrings = (''.join(random.choices(characters, k=length))for i in range(amount))
    return substrings

if __name__=="__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)