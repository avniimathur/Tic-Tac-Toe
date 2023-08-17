def analyseboard(board):
    # Check rows, columns, and diagonals to find a winner
    for row in board:
        if all(cell == '0' for cell in row):
            return 1
        if all(cell == 'X' for cell in row):
            return -1

    for col in range(3):
        if all(board[row][col] == '0' for row in range(3)):
            return 1
        if all(board[row][col] == 'X' for row in range(3)):
            return -1

    if all(board[i][i] == '0' for i in range(3)) or all(board[i][2 - i] == '0' for i in range(3)):
        return 1
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return -1

    return 0  # No winner found

def minimax(board, depth, is___maximizing):
    if analyseboard(board) == 1:
        return 1
    if analyseboard(board) == -1:
        return -1
    if analyseboard(board) == 0:
        return 0

    if is___maximizing:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = '0'
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = ''
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = ''
                    min_eval = min(min_eval, eval)
        return min_eval

def find__best__move(board):
    best__move = None
    best__eval = -float('inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'X'
                move_eval = minimax(board, 0, False)
                board[row][col] = ''
                if move_eval > best__eval:
                    best__eval = move_eval
                    best__move = (row, col)
    return best__move

def print__board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

print("Tic Tac Toe")
print__board(board)

while True:
    row, col = find__best__move(board)
    board[row][col] = '0'
    print("AI's move:")
    print__board(board)

    if analyseboard(board) == 1:
        print("AI is the Winner.")
        break
    elif analyseboard(board) == 0 and all(all(cell != '' for cell in row) for row in board):
        print("It's a draw!")
        break

    player_row = int(input("Enter row for your move (0, 1, or 2): "))
    player_col = int(input("Enter column for your move (0, 1, or 2): "))
    
    if board[player_row][player_col] == '':
        board[player_row][player_col] = 'X'
    else:
        print("This move is Invalid.")
        continue

    print__board(board)

    if analyseboard(board) == -1:
        print("You are the Winner.")
        break
    elif analyseboard(board) == 0 and all(all(cell != '' for cell in row) for row in board):
        print("It's a draw!")
        break
