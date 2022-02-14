# Write your solution here
from types import new_class


def no_vowels(my_string):
    vowels_list = ['a','e','u','i','o']
    new_string = ""
    for item in my_string:
        if item not in vowels_list:
            new_string += item
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))