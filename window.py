from tkinter import Tk, BOTH, Canvas

# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Line class
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color,
            width=2
        )

# Window class
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Generator")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
        self.__root.quit()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

# Main function
def main():
    win = Window(800, 600)

    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 100)
    p3 = Point(200, 200)
    p4 = Point(100, 200)

    # Create lines between the points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    # Draw the lines
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")
    win.draw_line(line4, "blue")

    # Keep the window open until closed
    win.wait_for_close()

# Entry point
if __name__ == "__main__":
    main()

