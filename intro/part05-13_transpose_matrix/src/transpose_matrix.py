# Write your solution here

def transpose(matrix: list):
    #rec = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    #matrix = rec
    temp = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if i < j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
if __name__ == "__main__":
    matrix = [  
        [1, 2, 3],
        [4, 5, 6], 
        [7, 8, 9]]
    print(transpose(matrix))

    matrix2 = [[1, 2], 
        [1, 2]]
    print(transpose(matrix2))
    print(transpose([[1, 2], [1, 2]]))
