from graphics import Window,Point,Line
from cell import Cell
from maze import Maze
def main():
    #win = Window(800, 600)
    #line1 = Line(Point(20,20),Point(100,100)) 
    #win.draw_line(line1,"black")
    """
    c = Cell(win)
    
    c.draw(50,50,100,100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125,125,200,200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225,225,250,250)

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(300,300,500,500)

    c.draw_move(c2,True)
    """

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)



    win.wait_for_close()


main()