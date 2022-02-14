# Write your solution here
def everything_reversed(my_list):
    rev_list = []
    i = len(my_list) - 1
    while i >= 0:
        rev_list.append(my_list[i][::-1])
        i -= 1
    return rev_list
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)