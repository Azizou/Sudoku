import random

class NonEmptyCell(Exception):
    pass
    
class Sudoku(object):
    """ This class represent the sodoku game object."""
    def __init__(self,board_size=9,level = 1):
        self.board_size = board_size
        self.EMPTY = '@'
        self.num_cells = board_size**2
        self.board = []
        self.make_board()
        self.level = level
        self.load_board()


    def make_board(self):
        self.board = []
        for i in range(self.board_size):
            self.board.append([self.EMPTY]*self.board_size)

    def place_digit(self,x,y,val):
        sutil = SudokuUtils()
        if self.board[x][y] == self.EMPTY:
            self.board[x][y] = val
            if sutil.check_row(self.board[x]) and sutil.check_row(sutil.get_column(y)) and sutil.check_row(sutil.get_block(x,y)):
                return True
            else:
                self.board[x][y] = self.EMPTY
                return False
        else:
            raise NonEmptyCell("Cell value cannot be override")
            
    
    def load_board(self):
        data = SudokuBoard(self.level).data
        for i in range(self.board_size):
            for j in range(self.board_size):
                if data[i*self.board_size +j]!='0':
                    self.board[i][j] = data[i*self.board_size +j]


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

class SudokuUtils(object):

    def __init(self,suodku):
        self.board = board
        self.sudoku = suodku
        self.board_size = suodku.board_size
    
    #Throws a value errors for values outside the 0 - 9 range
    def check_row(self,row):
        assert len(row)==self.board_size
        dct = {}
        for i in row:
            if int(i)<0 or int(i) > 9:
                raise ValueError
            if int(i)!= 0 and i in dct.keys():
                return False
            else:
                dct[i] = 1
        return True

    def check_rows(self):
        for row in range(self.board):
            if not self.check_row(row):
                return False
        return True
        
    def cehck_columns(self):
        for i in range(self.board_size):
            col = []
            for j in range(self.board_size):
                col.append(self.board[j][i])
            if not self.check_row(col):
                return False
        return True

    def check_block(self):
        pass

    def get_column(self, col):
        pass

    def get_block(self, row, col):
        pass


class SudokuSolver(object):

    def __init__(self,sudoku):
        self.sudoku = sudoku
        self.board = sudo.board
        self.board_size = sudoku.board_size

    def solve(self):
        pass

    
    
class SudokuBoard(object):

    def __init__(self,level):
        self.level = level
        self.data = []
        self.current = self.load_data()

    def load_data(self):
        x = random.randint(0,10000)
        dfile = open(str(self.level)+".txt","r")
        #naive solution
        lines = dfile.readlines()
        self.data = lines[x][:-1]
        dfile.close()
        return x

if __name__ == '__main__':
    Sudoku().display_board()
