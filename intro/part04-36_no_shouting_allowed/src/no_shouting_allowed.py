# Write your solution here
from types import new_class


def no_shouting(my_string):
    new_list = []
    for item in my_string:
        if item.isupper() == False:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)