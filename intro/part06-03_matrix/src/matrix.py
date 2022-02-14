# write your solution here
def read_file():
    with open("matrix.txt") as new_file:
        my_list = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            my_list.append(parts)
    return my_list

def matrix_sum():
    sum = 0
    matrix = read_file()
    for row in matrix:
        for item in row:
            sum += int(item)
    return sum

def matrix_max():
    list = []
    matrix = read_file()
    for row in matrix:
        for item in row:
            list.append(item)
    return int(max(list))

def row_sums():
    matrix = read_file()
    list = []
    for row in matrix:
        sum = 0
        for item in row:
            sum += int(item)
        list.append(sum)
    return list
            

if __name__ == "__main__":
    #print(row_sums())
    print(matrix_max())
