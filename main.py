from graphics import Window,Point,Line

def main():
    win = Window(800, 600)
    line1 = Line(Point(20,20),Point(100,100))
    win.draw_line(line1,"black")
    win.wait_for_close()

main()