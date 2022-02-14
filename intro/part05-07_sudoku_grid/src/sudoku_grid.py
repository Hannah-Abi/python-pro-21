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

def row_correct(sudoku: list, row_no: int):
    check = True
    for item in sudoku[row_no]:
        if sudoku[row_no].count(item) >1 and item != 0:
            check = False 
    return check

def block_correct(sudoku: list, row_no: int, column_no: int):
    same_list = []
    diff_list = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if sudoku[i][j] != 0:
                same_list.append(sudoku[i][j])
                if sudoku[i][j] not in diff_list:
                    diff_list.append(sudoku[i][j])
    if len(same_list) == len(diff_list):
        return True
    else:
        return False

def sudoku_grid_correct(sudoku: list):
    check1 = True
    check2 = True
    for i in range(9):
        if column_correct(sudoku, i) and row_correct(sudoku, i):
            check1 = True
        else:
            check1 = False
            break
    for i in range(0,7,3):
        for j in range(0,7,3):
            if block_correct(sudoku, i,j ) == False:
                check2 = False
                break
    if check1 and check2:
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku1 = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku1))

    sudoku = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))

    
