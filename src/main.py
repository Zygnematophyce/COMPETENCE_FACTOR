# coding: utf-8

"""
Author: Zygnematophyce
Based on radar chart from : https://en.wikipedia.org/wiki/Radar_chart
create a custom to do list competence.
"""

import tkinter as tk
import math


class MainWindow(tk.Tk):
    """ Create the main window. """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("Competence Factor")
        self.width = 500
        self.height = 550
        self.geometry("{}x{}".format(self.width,
                                     self.height))
                
        

#class FrameWidget(tk.Tk):
    

if __name__ == "__main__":
    print("competence factor")

    window = MainWindow()

    main_frame = tk.Frame(window)
    main_canvas = tk.Canvas(main_frame, bg="white", width=500, height=550)

    pos_x = window.width/2
    pos_y_init = 5
    long_line = 210

    # Create the main line.
    main_canvas.create_line(pos_x,
                            pos_y_init,
                            pos_x,
                            long_line)

    pos_y = pos_y_init

    # Create 10 transverses lines.
    for i in range(0, 11):
        main_canvas.create_line(pos_x - 10,
                                pos_y,
                                pos_x + 10,
                                pos_y)

        pos_y = long_line/10*i


    # Add trigonometric.
    x_center = window.width/2
    y_center = long_line
    
    degres = 0
    radian = math.radians(degres)

    # x = cos(radian)*r
    x_new = math.cos(radian)*long_line
    
    # y = sin(radian)*r
    y_new = math.sin(radian)*long_line

    # Centering the x and y points.
    x_new = x_new + x_center
    y_new = y_new + y_center


    main_canvas.create_line(x_center,
                            y_center,
                            x_new,
                            y_new)
    
    main_frame.pack()
    main_canvas.pack()

    window.mainloop()
