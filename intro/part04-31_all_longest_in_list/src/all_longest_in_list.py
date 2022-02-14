# Write your solution here
def all_the_longest(my_list):
    longest = my_list[0]
    res = []
    for i in range(len(my_list)-1):
        if len(my_list[i+1]) > len(longest):
            longest = my_list[i+1]
        i += 1
    res.append(longest)
    for item in my_list:
        if len(item) == len(longest) and item != longest:
            res.append(item)
    return res

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']