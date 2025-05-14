import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_break_entrance_and_exit(self):
   
        maze = Maze(3, 3, 10, 10, 10, 10)
        entrance_cell = maze._cells[0][0]
        exit_cell = maze._cells[9][9]  
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_maze_reset_cells_visited(self):
        num_cols = 15
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                self.assertEqual(
                    maze._cells[i][j].visited,
                    False,
                )
if __name__ == "__main__":
    unittest.main()