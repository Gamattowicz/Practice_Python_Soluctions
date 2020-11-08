board = [(['0']*3) for i in range(3)]


def draw_board(board):
    count = 0
    while count <= 9:
        while True:
            # Player 1
            move1 = input('Player 1 - Enter coordinates of your move [row, col]: ')
            move1 = move1.split(', ')
            if len(move1) == 2:
                m1_row = int(move1[0]) - 1
                m1_col = int(move1[1]) - 1
                if board[m1_row][m1_col] == '0':
                    board[m1_row][m1_col] = 'X'
                    print(board)
                    break
                else:
                    print('This place is not available. Try another place.')
            else:
                print('Coordinates should have only TWO values with comma and whitespace e.g. 1, 1')
        count += 1
        while True:
            # Player 2
            move2 = input('Player 2 - Enter coordinates of your move [row, col]: ')
            move2 = move2.split(', ')
            if len(move2) == 2:
                m2_row = int(move2[0]) - 1
                m2_col = int(move2[1]) - 1
                if board[m2_row][m2_col] == '0':
                    board[m2_row][m2_col] = 'o'
                    print(board)
                    break
                else:
                    print('This place is not available. Try another place.')
            else:
                print('Coordinates should have only TWO values with comma and whitespace e.g. 1, 1')
        count += 1


draw_board(board)
