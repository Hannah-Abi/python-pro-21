# Write your solution here
def histogram(texts):
    my_dictionary = {}
    for text in texts:
        if text not in my_dictionary:
            my_dictionary[text] = ""
        my_dictionary[text] += "*"
    for key, value in my_dictionary.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    histogram("statistically")
        