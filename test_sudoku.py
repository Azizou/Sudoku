#! /bin/env python3

import unittest
import sudoku
import copy

class TestSudoku(unittest.TestCase):

    def test_make_board(self):
        s = sudoku.Sudoku(2)
        s.make_board()                      # Initialize the board to empty cell
        result = [ [s.EMPTY, s.EMPTY],[s.EMPTY, s.EMPTY]]
        self.assertEqual(s.board, result, "Board format should be squared")

    def test_board_size(self):
        s = sudoku.Sudoku(2)
        self.assertEqual(s.num_cells,4)

    def test_load_evel(self):
        level = 2
        sb = sudoku.Sudoku(level=level)
        #There should be more than 36 empty slots
        self.assertTrue(sb.empties == 41)

    def test_protected_cell(self):
        s = sudoku.Sudoku()
        s.protected_cell[0] = 1
        with self.assertRaises(sudoku.NonEmptyCell):
            s.place_digit(0,0,'1')

    def test_place_number(self):
        s = sudoku.Sudoku(test=True)
        cp = copy.deepcopy(s.board)
        s.place_digit(2,2,'3')
        self.assertFalse(cp == s.board)
        s.board[2][2] = cp[2][2]
        self.assertTrue(cp == s.board)
	
    def test_complete_row(self):
        pass
	
    def test_filled_cells(self):
		"""In level 1 only 36 cells are empty"""
        s = sudoku.Sudoku(test=True)
        self.assertTrue(s.empties == 36)

if __name__ == '__main__':
    unittest.main()
