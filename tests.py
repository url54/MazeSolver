import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_create_cells_two(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertNotEqual(
            len(m1._Maze__cells),
            num_rows
        )
        self.assertNotEqual(
            len(m1._Maze__cells[0]),
            num_cols
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Set some cells as visited
        m1._Maze__cells[0][0].visited = True
        m1._Maze__cells[5][5].visited = True
        m1._Maze__cells[num_cols-1][num_rows-1].visited = True

        # Call the reset method
        m1._Maze__reset_cells_visited()

        # Verify all cells are now marked as not visited
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    m1._Maze__cells[i][j].visited,
                    f"Cell at position ({i}, {j}) should not be visited"
                )

if __name__ == "__main__":
    unittest.main()
