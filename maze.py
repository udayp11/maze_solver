from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
    
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j) 
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        cell_x = self._x1 + i*self._cell_size_x 
        cell_y = self._y1 + j*self._cell_size_y

        self._cells[i][j].draw(cell_x,cell_y,cell_x+self._cell_size_x,cell_y+self._cell_size_y)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols -1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1,self._num_rows -1 )

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            index_list = []

            if i>0 and not self._cells[i-1][j].visited:
                index_list.append((i-1,j))
            if i<self._num_cols - 1 and not self._cells[i+1][j].visited:
                index_list.append((i+1,j))
            if j>0 and not self._cells[i][j-1].visited:
                index_list.append((i,j-1))
            if j < self._num_rows -1 and not self._cells[i][j+1].visited:
                index_list.append((i,j+1))

            if len(index_list) == 0:
                self._draw_cell(i,j)
                return

            random_index = random.randrange(len(index_list))
            next_i,next_j = index_list[random_index]

            if next_i == i-1: #left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][j].has_right_wall = False
            if next_i == i +1 : #moving right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][j].has_left_wall = False
            if next_j == j-1: #up
                self._cells[i][j].has_top_wall = False
                self._cells[i][next_j].has_bottom_wall = False
            if next_j == j+1 :#down
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][next_j].has_top_wall = False

            self._break_walls_r(next_i,next_j)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False 

    

