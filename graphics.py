from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("My Maze Solver")
        self.__canvas = Canvas(self.__root,bg="white",height = self.height,width = self.width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self,line,fill_color="black"):
        line.draw(self.__canvas,fill_color)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,fill_color="black"):
        self.fill_color = fill_color
        canvas.create_line(
            self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=self.fill_color, width=2
        )


    


