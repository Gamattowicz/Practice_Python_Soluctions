board = [[2, 1, 1],
         [2, 0, 0],
         [2, 0, 0]]

winner_is_1 = [[0, 1, 0],
               [2, 1, 0],
               [2, 1, 1]]


def check(board):
    diagonal_1 = set([board[0][0], board[1][1], board[2][2]])
    diagonal_2 = set([board[0][2], board[1][1], board[2][0]])
    # rows
    for i in range(0, 3):
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != 0:
            return 'Player {} won'.format(board[i][0])
    # columns
    for i in range(0, 3):
        column = set([board[0][i], board[1][i], board[2][i]])
        if len(column) == 1 and board[0][i] != 0:
            return 'Player {} won'.format(board[0][i])
    # diagonals
    if len(diagonal_1) == 1 or len(diagonal_2) == 1 and board[1][1] != 0:
        return 'Player {} won'.format(board[1][1])
    return 'No winner'


print(check(board))
print(check(winner_is_1))
