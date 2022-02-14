# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    same_list = []
    diff_list = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if sudoku[i][j] != 0:
                same_list.append(sudoku[i][j])
                if sudoku[i][j] not in diff_list:
                    diff_list.append(sudoku[i][j])
    print(same_list)
    print(diff_list)
    if len(same_list) == len(diff_list):
        return True
    else:
        return False
if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))