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
    angle = 25
    radian = angle * (math.pi/180)

    cos_val = math.cos(radian)
    sin_val = math.sin(radian)

    print(y_cos)
    print(x_sin)

    main_canvas.create_line(pos_x,
                            long_line,
                            x_sin,
                            100)
    
    main_frame.pack()
    main_canvas.pack()

    window.mainloop()
