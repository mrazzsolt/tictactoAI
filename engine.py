from randomAI import randomAI
from checks import checks
import os


class board():
    def __init__(self,board):
        self.board = board
        self.board_height = 3
        self.board_width = 3

    def clear_board(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        c.board = [[None, None, None], [None, None, None], [None, None, None]]
    
    def render_board(self):
        os.system('cls')
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
        move = input("Next step [format 00 or 0 0]: ")
        if ' ' in move:
            move_coordinates = move.split()
        else:
            for x in move:
                move_coordinates.append(x)
        return move_coordinates


nextPlayer = False
b = board([[None, None, None], [None, None, None], [None, None, None]])
b.render_board()
m = takeMove()
c = checks(b.board)  # Pass the board to the checks class
r = randomAI()
def make_move_wrapper(player):
    if player == 'human':
        while True:
            move = m.input_move()
            if c.isLegalMove(move):
                b.make_move(move,'X')
                break
    if player == 'random_win_block_ai':
        while True:
            move = r.find_winning_move_wrapper(b.board,'O')
            #print(move)
            if c.isLegalMove(move):
                b.make_move(move,'O')
                break
    if player == 'random_ai':
        while True:
            move = r.send_random_move(b.board)
            #print(move)
            if c.isLegalMove(move):
                b.make_move(move,'O')
                break

while True:
    if not nextPlayer:
        make_move_wrapper('human')
        nextPlayer = True
    else:
        make_move_wrapper('random_win_block_ai')
        nextPlayer = False
    b.render_board()
    if c.getWinner():
        if nextPlayer:
            print('X won')
            break
        else:
            print('O won')
            break
    if c.isBoardFull():
        print('The board is full!')
        if not c.getWinner():
            print('Draw!')
            break
