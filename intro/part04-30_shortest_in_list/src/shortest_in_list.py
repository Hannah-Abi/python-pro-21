# Write your solution here
def shortest(my_list):
    shortest = my_list[0]
    for i in range(len(my_list)-1):
        if len(my_list[i+1]) < len(my_list[i]):
            shortest = my_list[i+1]
    return shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)