# Write your solution here
def most_common_character(my_list):
    count = my_list.count(my_list[0])
    max_count = my_list[0]
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) > count:
            count = my_list.count(my_list[i])
            max_count = my_list[i]
    return max_count
        
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))