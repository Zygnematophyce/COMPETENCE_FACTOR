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
    main_canvas = tk.Canvas(main_frame, bg="ivory", width=500, height=550)

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
        main_canvas.create_line(pos_x - 5,
                                pos_y,
                                pos_x + 5,
                                pos_y)

        pos_y = long_line/10*i


    # Add trigonometric.
    x_center = window.width/2
    y_center = long_line
    
    degres = 10
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

    # The degrees to be subtracted from the degree
    # of the main line.
    radian_substract = math.radians(90)
    
    # Create 10 transverses lines.
    for i in range(1, 11):
        # Adding all points centered on the main line.
        try:
            point_x_center = ((long_line * (10*i) /100) * math.cos(radian)) + x_center
            point_y_center = ((long_line * (10*i) /100) * math.sin(radian)) + y_center
        except ZeroDivisionError as e:
            print(e)
            point_x_center = x_center
            point_y_center = y_center

        # Create the first points of line.
        xa_coord_line = 5 * math.cos(radian - radian_substract) + point_x_center
        ya_coord_line = 5 * math.sin(radian - radian_substract) + point_y_center

        # Create the second points of line.
        xb_coord_line = 5 * -1 * math.cos(radian - radian_substract) + point_x_center
        yb_coord_line = 5 * -1 * math.sin(radian - radian_substract) + point_y_center
    
        # Plot all transverses lines.
        main_canvas.create_line(xa_coord_line,
                                ya_coord_line,
                                xb_coord_line,
                                yb_coord_line)

    main_frame.pack()
    main_canvas.pack()

    window.mainloop()
