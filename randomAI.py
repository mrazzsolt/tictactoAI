import random
import checks

class randomAI():
    def __init__(self):
        self.board_height = 3
        self.board_width = 3

    def send_random_move(self,board):
        num_columns = len(board[0])
        random.seed()
        indexes = checks.getAllLegalMove(board)
        position = random.randint(indexes[0], indexes[-1])
        row = position // num_columns
        col = position % num_columns
        print(f"Index {position} corresponds to row {row}, column {col}")
        return [row,col]
    
    def isLegalMove(self,board,step):
        return checks.isLegalMove(board, step)
    
    def find_winning_move_wrapper(self,board,ai_mark):
        return self.find_winning_move(board, ai_mark, 0, 1)

    def find_winning_move(self,board,ai_mark,depth,max_depth):
        if depth > max_depth:
            return None
        r = randomAI() 
        cross_values = []
        cross_values_none_index = -1
        reverse_cross_values = []
        reverse_cross_values_none_index = []

        for x in range(self.board_width):

            column_values = [row[x] for row in board]
            if column_values.count(ai_mark) == 2 and column_values.count(None) == 1:
                if r.isLegalMove(board,[column_values.index(None),x]):
                    print(f'Send this move {x}{column_values.index(None)}')
                    return [column_values.index(None),x]

            row_values = board[x]
            if row_values.count(ai_mark) == 2 and row_values.count(None) == 1:
                if r.isLegalMove(board,[x,row_values.index(None)]):
                    print(f'Send this move2 {x}{row_values.index(None)}')
                    return [x,row_values.index(None)]
                
            cross_values.append(board[x][x])
            if board[x][x] is None:
                cross_values_none_index = x
            reverse_cross_values.append(board[x][self.board_width-x-1])
            if board[x][self.board_width-x-1] is None:
                reverse_cross_values_none_index.append(x)
                reverse_cross_values_none_index.append(self.board_width-x-1)

        if cross_values.count(ai_mark) == 2 and cross_values.count(None) == 1:
            if r.isLegalMove(board,[cross_values_none_index,cross_values_none_index]):
                return [cross_values_none_index,cross_values_none_index]
        
        if reverse_cross_values.count(ai_mark) == 2 and reverse_cross_values.count(None) == 1:
            if r.isLegalMove(board,reverse_cross_values_none_index):
                return reverse_cross_values_none_index
        if depth == 1:
            return r.send_random_move(board)
        return r.find_winning_move(board,'X',depth+1,max_depth)
