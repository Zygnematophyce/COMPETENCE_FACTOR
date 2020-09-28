# coding: utf-8

"""
Author: Zygnematophyce

"""

import tkinter as tk


class MainWindow(tk.Tk):
    """ Create the main window. """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("Competence Factor")
        self.width = 200
        self.height = 250
        self.geometry("{}x{}".format(self.width,
                                     self.height))
                
        

#class FrameWidget(tk.Tk):
    

if __name__ == "__main__":
    print("competence factor")

    window = MainWindow()

    main_frame = tk.Frame(window)
    main_canvas = tk.Canvas(main_frame)

    # x0, y0, x1, y1
    main_canvas.create_line(150, 0, 150, 150)
    main_canvas.create_line(0, 50, 150, 50)

    main_frame.pack()
    main_canvas.pack()

    window.mainloop()
