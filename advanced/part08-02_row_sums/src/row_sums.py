# Write your solution here
def row_sums(my_matrix: list):
    for s in my_matrix:
        s.append(sum(s))
    
if __name__=="__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)