#There is a problem when someone win. If win Player 1, communicate prited 2 times. 

board = [(['0']*3) for i in range(3)]


def game_board(board):
        print(' -'*3)
        print('|' + board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '|')
        print(' -'*3)
        print('|' + board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '|')
        print(' -'*3)
        print('|' + board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '|')
        print(' -'*3)


def check_board(board):
    diagonal_1 = set([board[0][0], board[1][1], board[2][2]])
    diagonal_2 = set([board[0][2], board[1][1], board[2][0]])
    # rows
    for i in range(0, 3):
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != '0':
            print('Player {} won'.format(1 if board[i][0] == 'X' else 2))
            return 1
    # columns
    for i in range(0, 3):
        column = set([board[0][i], board[1][i], board[2][i]])
        if len(column) == 1 and board[0][i] != '0':
            print('Player {} won'.format(1 if board[0][i] == 'X' else 2))
            return 1
    # diagonals
    if (len(diagonal_1) == 1 or len(diagonal_2) == 1) and board[1][1] != '0':
        print('Player {} won'.format(1 if board[1][1] == 'X' else 2))
        return 1
    return 0


def draw_board(board):
    count = 0
    while count <= 9 and check_board(board) != 1:
        while True:
            # Player 1
            move1 = input('Player 1 - Enter coordinates of your move [row, col]: ')
            move1 = move1.split(', ')
            if len(move1) == 2:
                m1_row = int(move1[0]) - 1
                m1_col = int(move1[1]) - 1
                if board[m1_row][m1_col] == '0':
                    board[m1_row][m1_col] = 'X'
                    game_board(board)
                    break
                else:
                    print('This place is not available. Try another place.')
                    game_board(board)
            else:
                print('Coordinates should have only TWO values with comma and whitespace e.g. 1, 1')
        count += 1
        while check_board(board) != 1:
            # Player 2
            move2 = input('Player 2 - Enter coordinates of your move [row, col]: ')
            move2 = move2.split(', ')
            if len(move2) == 2:
                m2_row = int(move2[0]) - 1
                m2_col = int(move2[1]) - 1
                if board[m2_row][m2_col] == '0':
                    board[m2_row][m2_col] = 'o'
                    game_board(board)
                    break
                else:
                    print('This place is not available. Try another place.')
                    game_board(board)
            else:
                print('Coordinates should have only TWO values with comma and whitespace e.g. 1, 1')
        count += 1


draw_board(board)
