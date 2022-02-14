# Write your solution here
def formatted(my_list):
    str_list = []
    #for i in range(len(my_list)):
        #str_list.append((round(my_list[i],2)))
    for item in my_list:
        str_list.append(f"{item:.2f}")
    return str_list
if __name__ == "__main__":
    my_list = [1.222, 0.33333, 0.6666, 0.9999]
    new_list = formatted(my_list)
    print(new_list)
