# Write your solution here
def column_correct(sudoku: list, column_no: int):
    list1 = []
    list2 = []
    for row in sudoku:
        if row[column_no] not in list1 and row[column_no] != 0:
            list1.append(row[column_no])
        if row[column_no] != 0:
            list2.append(column_no)
    if len(list1) == len(list2):
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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))