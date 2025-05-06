import unittest
from maze_gui import Maze

class TestMaze(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 4, 4, 10, 10)
        maze._break_entrance_and_exit()
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 3, 3, 10, 10)
        for col in maze._cells:
            for cell in col:
                cell.visited = True
        maze._reset_cells_visited()
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell.visited)

    def test_maze_solver(self):
        maze = Maze(0, 0, 5, 5, 10, 10, seed=0)
        result = maze.solve()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

