from randomAI import randomAI

class board():
    def __init__(self,board):
        self.board = board
        self.board_height = 3
        self.board_width = 3

    def clear_board(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        c.board = [[None, None, None], [None, None, None], [None, None, None]]
    
    def render_board(self):
        print('   0 1 2 ')
        print('  ------')
        rows = []
        for x in range(0,self.board_height):
            row = []
            for y in range(0,self.board_width):
                row.append(self.board[x][y])
            rows.append(row)
        row_num = 0

        for row in rows:
            output_row = ''
            for nm in row:
                if nm is None:
                    output_row += ' '
                else:
                    output_row += nm
            print("%d|%s |" % (row_num, ' '.join(output_row)))
            row_num += 1
        print('  ------')

    def make_move(self,inp,xOrY):
        intinp = []
        for x in inp:
            intinp.append(int(x))
        self.board[intinp[0]][intinp[1]] = xOrY

class takeMove():
    def __init__(self):
        self.move = []
    
    def input_move(self):
        move_coordinates = []
        move = input("Kérem a következő lépést: ")
        if ' ' in move:
            move_coordinates = move.split()
        else:
            for x in move:
                move_coordinates.append(x)
        return move_coordinates

class checks():  
    def __init__(self):
        self.board = b.board
    
    def isLegalMove(self,step):
        intStep = []
        for x in step:
            intStep.append(int(x))
        if len(intStep) > 2:
            print('Helytelen lépés!')
            return False
        if intStep[0]+1 > b.board_height  or intStep[1]+1 > b.board_width:
            print('Helytelen lépés!')
            return False 
        #print(intStep)
        if self.board[intStep[0]][intStep[1]] is None:
            return True
        else:
            print('Helytelen lépés!')
            return False
    
    def isBoardFull(self):
        for x in self.board:
            for y in x:
                if y is None:
                    return False
        return True
    
    def checkRow(self, lst):
        return lst[0] is not None and all(x == lst[0] for x in lst)


    def checkColumn(self,board, col_index):
        # Get the values in the specified column
        column_values = [row[col_index] for row in board]
        # Check if all values in the column are the same
        return column_values[0] is not None and all(val == column_values[0] for val in column_values)
    
    def checkPrimaryDiagonal(self):
        # Ensure all elements in the primary diagonal are the same and not None
        return self.board[0][0] is not None and all(self.board[i][i] == self.board[0][0] for i in range(len(self.board)))

    def checkSecondaryDiagonal(self):
        n = len(self.board)
        # Ensure all elements in the secondary diagonal are the same and not None
        return self.board[0][n-1] is not None and all(self.board[i][n-i-1] == self.board[0][n-1] for i in range(n))

    
    def getWinner(self):
        c = checks()
        for x in self.board:
            #print(x)
            if c.checkRow(x):
                return True
        
        for x in range(3):
            if c.checkColumn(self.board,x):
                return True
        if c.checkPrimaryDiagonal():
            return True
        if c.checkSecondaryDiagonal():
            return True
        return False
        

nextPlayer = False
b = board([[None, None, None], [None, None, None], [None, None, None]])
m = takeMove()
c = checks()
r = randomAI()
while True:
    if not nextPlayer:
        while True:
            move = m.input_move()
            if c.isLegalMove(move):
                b.make_move(move,'X')
                break
        nextPlayer = True
    else:
        while True:
            move = r.find_winning_move_wrapper(b.board,'O')
            #print(move)
            if c.isLegalMove(move):
                b.make_move(move,'O')
                break
        nextPlayer = False
    b.render_board()
    if c.getWinner():
        if nextPlayer:
            print('X won')
            restart = input('Wanna play again?')
            if restart == 'y':
                b.clear_board()
            else:
                break
        else:
            print('O won')
            restart = input('Wanna play again?')
            if restart == 'y':
                b.clear_board()
            else:
                break
    if c.isBoardFull():
        print('The board is full!')
        if not c.getWinner():
            print('Döntetlen')
            restart = input('Wanna play again?')
            if restart == 'y':
                b.clear_board()
            else:
                break
