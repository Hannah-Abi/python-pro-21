# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        my_list = []
        for line in new_file:
            line = line.replace("\n", "")
            my_list.append(line)
    return int(max(my_list))

if __name__ == "__main__":
    largest()