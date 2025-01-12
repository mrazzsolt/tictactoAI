import copy

def make_move(board, inp, xOrY):
    intinp = [int(x) for x in inp]
    board[intinp[0]][intinp[1]] = xOrY

def get_winner(board):
    all_line_co_ords = get_all_line_co_ords()
    for line in all_line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]
    return None

def get_all_line_co_ords():
    cols = []
    for x in range(0, 3):
        col = []
        for y in range(0, 3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append((x, y))
        rows.append(row)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return cols + rows + diagonals

def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is None:
                return False
    return True

def getAllLegalMove(board):
    indexes = []
    for index, cell in enumerate([elem for row in board for elem in row]):
        if cell is None:
            indexes.append(index)
    return indexes

def minimax(board, markAI):
    best_move = None
    best_score = None
    num_columns = len(board[0])
    legalmoves = []
    indexes = getAllLegalMove(board)
    for x in indexes:
        row = x // num_columns
        col = x % num_columns
        legalmoves.append([row, col])

    for move in legalmoves:
        _board = copy.deepcopy(board)
        make_move(_board, move, markAI)  # Make move on the copied board
        opp = 'X' if markAI == 'O' else 'O'  # Alternate opponent
        score = _minimax_score(_board, opp, markAI)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move

def _minimax_score(board, player_to_move, player_to_optimize):
    legalmoves = []
    num_columns = len(board[0])
    winner = get_winner(board)
    
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif is_board_full(board):
        return 0

    indexes = getAllLegalMove(board)
    for x in indexes:
        row = x // num_columns
        col = x % num_columns
        legalmoves.append([row, col])

    scores = []
    for move in legalmoves:
        _board = copy.deepcopy(board)
        make_move(_board, move, player_to_move)
        opp = 'X' if player_to_move == 'O' else 'O'
        opp_best_response_score = _minimax_score(_board, opp, player_to_optimize)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)
