import random
class Sudoku(object):
    """ This class represent the sodoku game object."""
    def __init__(self,board_size=9,level = 1):
        self.board_size = board_size
        self.num_cells = board_size**2
        self.board = []
        self.make_board()
        self.level = level
        self.load_board()


    def make_board(self):
        self.board = []
        for i in range(self.board_size):
            self.board.append([' ']*self.board_size)

    def load_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if data[i*self.board_size +j]!='0':
                    self.board[i][j] = data[i*self.board_size +j]


    def display_board(self):
        data = SudokuBoard(self.level).data
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.board[i][j], end='  ')
            print("enddddd")


class SudokuBoard(object):

    def __init__(self,level):
        self.level = level
        self.data = self.load_data()

    def load_data(self):
        x = random.randint(0,10000)
        dfile = open(str(self.level)+".txt","r")
        #naive solution
        lines = dfile.readlines()
        data = lines[x][:-1]
        dfile.close()
        return data
