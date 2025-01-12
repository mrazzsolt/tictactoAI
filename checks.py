class checks():  
    def __init__(self, board):
        self.board = board
        self.board_height = 3
        self.board_width = 3
    
    def isLegalMove(self, step):
        intStep = []
        for x in step:
            intStep.append(int(x))
        if len(intStep) > 2:
            print('Invalid step!')
            return False
        if intStep[0]+1 > self.board_height or intStep[1]+1 > self.board_width:
            print('Invalid step!')
            return False 
        if self.board[intStep[0]][intStep[1]] is None:
            return True
        else:
            print('Invalid step!')
            return False
    
    def isBoardFull(self):
        for x in self.board:
            for y in x:
                if y is None:
                    return False
        return True
    
    def checkRow(self, lst):
        return lst[0] is not None and all(x == lst[0] for x in lst)

    def checkColumn(self, board, col_index):
        column_values = [row[col_index] for row in board]
        return column_values[0] is not None and all(val == column_values[0] for val in column_values)
    
    def checkPrimaryDiagonal(self):
        return self.board[0][0] is not None and all(self.board[i][i] == self.board[0][0] for i in range(len(self.board)))

    def checkSecondaryDiagonal(self):
        n = len(self.board)
        return self.board[0][n-1] is not None and all(self.board[i][n-i-1] == self.board[0][n-1] for i in range(n))
   
    def getWinner(self):
        for x in self.board:
            if self.checkRow(x):
                return True
        
        for x in range(3):
            if self.checkColumn(self.board, x):
                return True
        if self.checkPrimaryDiagonal():
            return True
        if self.checkSecondaryDiagonal():
            return True
        return False
