#from enum import Enum
import random, math
class NonEmptyCell(Exception):
    pass
"""
class Status(Enum):
    ''' Represent the status of the game given the current change or event'''
    success    = 1
    error      = 2
    complete   = 3
    invalid    = 4
 """   
class Sudoku(object):
    """ This class represent the sodoku game object."""
    def __init__(self,board_size=9,level = 1,test = False):
        self.board_size = board_size
        self.EMPTY = '0'
        self.empties = 0
        self.test = test
        self.protected_cell = dict()
        self.num_cells = board_size**2
        self.board = []
        self.make_board()
        self.level = level
        self.load_board()


    def make_board(self):
        self.board = []
        self.protected_cell = dict()
        for i in range(self.board_size):
            self.board.append([self.EMPTY]*self.board_size)

    def place_digit(self,x,y,val):
        #sutil = SudokuUtils(self.board, self.board_size)
        currVal = self.board[y][x]
        if not self.protected_cell[y*self.board_size +x]:
            #assert val in list(range(self.board_size +1))
            #set the val at x y
            self.board[y][x] = val
            #Check if move is legal            
            if self.check(self.get_row(y)) and self.check(self.get_column(x)) and self.check(self.get_block(y,x)):
                self.empties += 1
                return True 
            else:
            # Undo change
                
                self.board[y][x] = currVal
                return False
        else:
            raise NonEmptyCell("Cell value cannot be modified")
            
    
    def load_board(self):
        if self.test:
            data = SudokuBoard(self.level,True).data
        else:
            data = SudokuBoard(self.level).data
        for i in range(self.board_size):
            for j in range(self.board_size):
                if data[i*self.board_size +j]!='0':
                    #Player cannot modify this cell later on
                    self.protected_cell[i*self.board_size +j] = 1 # Mark cell as protected
                    self.board[i][j] = data[i*self.board_size +j]
                else:
                    # Cell value is editable by player
                    self.empties += 1
                    self.protected_cell[i*self.board_size +j] = 0


    def display_board(self):
        print("    |A1 |A2 |A3 |A4 |A5 |A6 |A7 |A8 |A9 |")
        for i in range(self.board_size):
            print("----"*10 + "-")
            print(' B',i+1, sep='',end= ' ')
            for j in range(self.board_size):
                print("| " + self.board[i][j], end=' ')
            print("|")
        print("----"*10 + "-")
        print()


    #Throws a value errors for values outside the 0 - 9 range
    def check_complete_row(self, a_row):
        vals = [int(a) for a in a_row]
        return sum(vals) == self.board_size*(self.board_size +1)/2

    def check(self,a_row):
        #assert len(row)==self.board_size
        dct = {}
        for i in a_row:
            if int(i)<0 or int(i) > 9:
                raise ValueError
            if int(i)!= 0 and i in dct.keys():
                return False
            else:
                dct[i] = 1
        return True

    def check_rows(self):
        for row in range(self.board):
            if not self.check_complete_row(row):
                return False
        return True
        
    def cehck_columns(self):
        for i in range(self.board_size):
            if not self.check_complete_row(self.get_column(col)):
                return False
        return True

    def check_block(self):
        block_width = math.floor(math.sqrt(self.board_size))
        for i in range(0,self.board_size,block_width):
            for j in range(0,self.board_size,block_width):
                if not self.check_complete_row(self.get_block(i,j)):
                    return False
        return True

    def get_row(self, row):
        return self.board[row]

    def get_column(self, col):
        result = []
        for i in range(self.board_size):
            result.append(self.board[i][col])
        return result

    def get_block(self, row, col):
        block_width = math.floor(math.sqrt(self.board_size))
        row = (row//block_width)*block_width
        col = (col//block_width)*block_width
        result = []
        for i in range(row,row + block_width):
            for j in range(col,col + block_width):
                result.append(self.board[i][j])
        return result

class SudokuUtils(object):
    """ Helper functions for the sudoku game """
    def __init__(self,board,board_size):
        self.board = board
        #self.sudoku = suodku
        self.board_size = board_size
    


class SudokuSolver(object):

    def __init__(self,sudoku):
        self.sudoku = sudoku
        self.board = sudo.board
        self.board_size = sudoku.board_size

    def solve(self):
        pass

    
    
class SudokuBoard(object):
    '''Load board from file'''
    def __init__(self,level,test=False):
        self.level = level
        self.data = []
        self.test = test
        self.current = self.load_data()

    def load_data(self):
        if not self.test:
            x = random.randint(0,10000)
        else:
            x = 533
        print("Line",x,"will be loaded")
        dfile = open(str(self.level)+".txt","r")
        #naive solution try fseek and ftell
        lines = dfile.readlines()
        self.data = lines[x][:-1]
        dfile.close()
        return x

if __name__ == '__main__':
    s = Sudoku()
    s.display_board()
##    print(s.empties)
##    print(s.place_digit(2,2,'1'))
##    print(s.empties)
##    s.display_board()
