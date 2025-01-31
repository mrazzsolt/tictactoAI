def getAllLegalMove(board):
    indexes = []
    for index, cell in enumerate([elem for row in board for elem in row]):
        if cell is None:
            indexes.append(index)
    return indexes

def isLegalMove(board, step):
    intStep = [int(x) for x in step]
    if len(intStep) > 2:
        print('Invalid step!')
        return False
    if intStep[0] + 1 > 3 or intStep[1] + 1 > 3:
        print('Invalid step!')
        return False
    if board[intStep[0]][intStep[1]] is None:
        return True
    else:
        print('Invalid step!')
        return False

def isBoardFull(board):
    for x in board:
        for y in x:
            if y is None:
                return False
    return True

def checkRow(lst):
    return lst[0] is not None and all(x == lst[0] for x in lst)

def checkColumn(board, col_index):
    column_values = [row[col_index] for row in board]
    return column_values[0] is not None and all(val == column_values[0] for val in column_values)

def checkPrimaryDiagonal(board):
    return board[0][0] is not None and all(board[i][i] == board[0][0] for i in range(len(board)))

def checkSecondaryDiagonal(board):
    n = len(board)
    return board[0][n-1] is not None and all(board[i][n-i-1] == board[0][n-1] for i in range(n))

def getWinner(board):
    for x in board:
        if checkRow(x):
            return True

    for x in range(3):
        if checkColumn(board, x):
            return True
    if checkPrimaryDiagonal(board):
        return True
    if checkSecondaryDiagonal(board):
        return True
    return False
