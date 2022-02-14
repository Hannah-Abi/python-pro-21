# Write your solution here
def  copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    copy_sudoku = []
    block = []
    count = 0
    for row in sudoku:
        for item in row:
            new_sudoku.append(item)
    while count in range(81):
        block = new_sudoku[count:count+9]
        copy_sudoku.append(block)
        count += 9
    copy_sudoku[row_no][column_no] = number
    return copy_sudoku

def print_sudoku(sudoku: list):
    i, j= 0, 0
    for row in sudoku:
        j += 1
        for item in row:
            i += 1
            if item == 0:
                item = "_"
            print(f"{item}", end = " ")
            if i%3 == 0:
                print(" ", end = "")
        print()
        if j%3 == 0:
            print()
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
