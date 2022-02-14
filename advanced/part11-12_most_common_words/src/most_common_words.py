# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    word_list = []
    with open(filename) as word_file:
        for line in word_file:
            line = line.replace("\n", "")
            line = line.replace(".", "")
            line = line.replace(",", "")
            line = line.split() 
            word_list += line
    return {word: word_list.count(word) for word in word_list if word_list.count(word) >= lower_limit}
    #return word_list

if __name__=="__main__":
    print(most_common_words("comprehensions.txt", 3))