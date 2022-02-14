# Write your solution here
def length_of_longest(my_list):
    len_list = []
    for item in my_list:
        len_list.append(len(item))
    return max(len_list)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)