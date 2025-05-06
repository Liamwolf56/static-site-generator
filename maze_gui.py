from tkinter import Tk, Canvas
import time
import random

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is not None:
            color = "black"
            if self.has_left_wall:
                self._win.create_line(self._x1, self._y1, self._x1, self._y2, fill=color)
            else:
                self._win.create_line(self._x1, self._y1, self._x1, self._y2, fill="#d9d9d9")
            if self.has_right_wall:
                self._win.create_line(self._x2, self._y1, self._x2, self._y2, fill=color)
            else:
                self._win.create_line(self._x2, self._y1, self._x2, self._y2, fill="#d9d9d9")
            if self.has_top_wall:
                self._win.create_line(self._x1, self._y1, self._x2, self._y1, fill=color)
            else:
                self._win.create_line(self._x1, self._y1, self._x2, self._y1, fill="#d9d9d9")
            if self.has_bottom_wall:
                self._win.create_line(self._x1, self._y2, self._x2, self._y2, fill=color)
            else:
                self._win.create_line(self._x1, self._y2, self._x2, self._y2, fill="#d9d9d9")

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._cols):
            column = []
            for j in range(self._rows):
                x1 = self._x1 + (i * self._cell_size_x)
                y1 = self._y1 + (j * self._cell_size_y)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                column.append(cell)
                cell.draw()
            self._cells.append(column)

    def _animate(self):
        if self._win:
            self._win.update()
            time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            neighbors = []
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))
            if i < self._cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            if j < self._rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))

            if not neighbors:
                current.draw()
                return

            ni, nj = random.choice(neighbors)
            next_cell = self._cells[ni][nj]

            if ni == i - 1:
                current.has_left_wall = False
                next_cell.has_right_wall = False
            elif ni == i + 1:
                current.has_right_wall = False
                next_cell.has_left_wall = False
            elif nj == j - 1:
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif nj == j + 1:
                current.has_bottom_wall = False
                next_cell.has_top_wall = False

            current.draw()
            next_cell.draw()
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if i == self._cols - 1 and j == self._rows - 1:
            return True

        directions = [
            ("left", i - 1, j, not current.has_left_wall),
            ("right", i + 1, j, not current.has_right_wall),
            ("top", i, j - 1, not current.has_top_wall),
            ("bottom", i, j + 1, not current.has_bottom_wall),
        ]

        for direction, ni, nj, can_go in directions:
            if 0 <= ni < self._cols and 0 <= nj < self._rows and can_go:
                neighbor = self._cells[ni][nj]
                if not neighbor.visited:
                    self._draw_move(i, j, ni, nj, "green")
                    if self._solve_r(ni, nj):
                        return True
                    self._draw_move(i, j, ni, nj, "red")

        return False

    def _draw_move(self, i1, j1, i2, j2, color):
        if self._win is None:
            return

        x1 = self._cells[i1][j1]._x1 + self._cell_size_x // 2
        y1 = self._cells[i1][j1]._y1 + self._cell_size_y // 2
        x2 = self._cells[i2][j2]._x1 + self._cell_size_x // 2
        y2 = self._cells[i2][j2]._y1 + self._cell_size_y // 2

        self._win.create_line(x1, y1, x2, y2, fill=color, width=2)
        self._animate()

if __name__ == "__main__":
    root = Tk()
    root.title("Maze")
    canvas = Canvas(root, width=600, height=600, bg="#d9d9d9")
    canvas.pack()

    maze = Maze(10, 10, 10, 10, 50, 50, win=canvas, seed=0)

    solved = maze.solve()
    print("Solved!" if solved else "No solution found.")

    root.mainloop()

