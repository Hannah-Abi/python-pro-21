# Write your solution here
def who_won(game_board: list):
    score1 = 0
    score2 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                score1 += 1
            if square == 2:
                score2 += 1
    if score1 > score2:
        return 1
    elif score1 <score2:
        return 2
    else:
        return 0