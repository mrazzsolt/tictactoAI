#board =[['X', 'O', 'O'], ['X', 'O', 'O'], ['X', 'X', 'X']]
#def all_same(lst):
#    return all(x == lst[0] for x in lst)
#
#
#
#def check_column(board, col_index):
#    # Get the values in the specified column
#    column_values = [row[col_index] for row in board]
#    # Check if all values in the column are the same
#    return all(val == column_values[0] for val in column_values)
#
#for x in board:
#    print(all_same(x))
#
#print(board[1][0])
#
#if check_column(board, 1):  # Check the first column (index 0)
#    print("Yes")
#else:
#    print("No")
#
#for x in range(3):
#    print(x)
#
#c = [0,1,3]
#print('')
#print(len(c))

import random

board = [['X', 'O', 'O'], ['X', None, 'O'], ['X', 'X', 'X']]

# Number of columns in the board
num_columns = len(board[0])  # Assuming all rows have the same number of columns

for index, cell in enumerate([elem for row in board for elem in row]):
    print(f"Index: {index}, Value: {cell}")
random.seed()
print(random.randint(3, 9))

# Example: Selecting index 4
index = 4

# Convert back to row and column
row = index // num_columns
col = index % num_columns

print(f"Index {index} corresponds to row {row}, column {col}")
