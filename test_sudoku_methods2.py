import unittest
import sudoku

class TestSudokuMethods(unittest.TestCase):

    def test_make_board(self):
        s = sudoku.Sudoku(2)
        s.make_board()
        result = [ [s.EMPTY, s.EMPTY],[s.EMPTY, s.EMPTY]]
        self.assertEqual(s.board, result)

    def test_board_size(self):
        s = sudoku.Sudoku(2)
        self.assertEqual(s.num_cells,4)

    def test_load_level(self):
        level = 1
        sb = sudoku.SudokuBoard(level)
        self.assertTrue(len(sb.data)==81)

if __name__ == '__main__':
    unittest.main()
