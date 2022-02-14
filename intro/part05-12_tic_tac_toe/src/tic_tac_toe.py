# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x in range(0,3) and y in range(0,3):
        if game_board[y][x] == '':
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    game_board = [['', '', 'X'], ['X', '', 'O'], ['O', 'O', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)

    game_board = [['O', '', 'X'], ['', 'O', 'O'], ['X', '', '']]
    print(play_turn(game_board, 2, -1, "X"))
    print(game_board)