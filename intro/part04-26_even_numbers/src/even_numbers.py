# Write your solution here
def even_numbers(my_list):
    even_list = []
    for item in my_list:
        if item%2 == 0:
            even_list.append(item)
    return even_list

if __name__ == "__main__":
    my_list = [2, 4, 8, 10, 12, 14]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)