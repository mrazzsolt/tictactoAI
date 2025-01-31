import copy
import checks as c

def execute_move(grid, position, symbol):
    int_position = [int(x) for x in position]
    grid[int_position[0]][int_position[1]] = symbol

# Függvény a győztes ellenőrzésére
def determine_winner(grid):
    all_lines = generate_all_lines()  # Az összes lehetséges nyerő vonal koordinátái
    for line in all_lines:
        values = [grid[x][y] for (x, y) in line]  # Kigyűjtjük a vonal értékeit
        if len(set(values)) == 1 and values[0] is not None:
            return values[0]
    return None  # Ha nincs győztes, None-t adunk vissza

# Függvény az összes lehetséges nyerő vonal generálására
def generate_all_lines():
    columns = []
    for x in range(0, 3):
        column = []
        for y in range(0, 3):
            column.append((x, y))
        columns.append(column)

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
    return columns + rows + diagonals

# Függvény a legjobb lépés megtalálására az AI számára
def minimax(grid, ai_symbol):
    best_action = None
    best_score = None
    num_cols = len(grid[0])
    possible_actions = []

    # Az összes lehetséges lépés koordinátáinak kiszámítása
    valid_indices = c.getAllLegalMove(grid)
    for index in valid_indices:
        row = index // num_cols
        col = index % num_cols
        possible_actions.append([row, col])

    # Minden lehetséges lépés kiértékelése
    for action in possible_actions:
        temp_grid = copy.deepcopy(grid)  # Másolat készítése a tábláról
        execute_move(temp_grid, action, ai_symbol)  # Lépés végrehajtása a másolaton
        opponent_symbol = 'X' if ai_symbol == 'O' else 'O'
        score = evaluate_move(temp_grid, opponent_symbol, ai_symbol)  # Pontszám kiszámítása
        if best_score is None or score > best_score:  # Ha ez a lépés jobb, mint az eddigi legjobb
            best_action = action
            best_score = score

    return best_action

# Függvény a lépés pontszámának kiszámítására
def evaluate_move(grid, current_player, target_player):
    possible_actions = []
    num_cols = len(grid[0])
    winner = determine_winner(grid)

    # Ha van győztes, visszaadjuk a megfelelő pontszámot
    if winner is not None:
        if winner == target_player:
            return 10  # Ha a céljátékos nyert, 10 pont
        else:
            return -10  # Ha az ellenfél nyert, -10 pont
    elif c.isBoardFull(grid):
        return 0  # Döntetlen esetén 0 pont

    # Az összes lehetséges lépés koordinátáinak kiszámítása
    valid_indices = c.getAllLegalMove(grid)
    for index in valid_indices:
        row = index // num_cols
        col = index % num_cols
        possible_actions.append([row, col])

    scores = []  # Az összes lehetséges lépés pontszámai
    for action in possible_actions:
        temp_grid = copy.deepcopy(grid)  # Másolat készítése a tábláról
        execute_move(temp_grid, action, current_player)  # Lépés végrehajtása a másolaton
        opponent_symbol = 'X' if current_player == 'O' else 'O'
        opponent_score = evaluate_move(temp_grid, opponent_symbol, target_player)  # Ellenfél pontszáma
        scores.append(opponent_score)

    # Ha a céljátékos van soron, a maximális pontszámot választjuk
    if current_player == target_player:
        return max(scores)
    else:  # Ha az ellenfél van soron, a minimális pontszámot választjuk
        return min(scores)
