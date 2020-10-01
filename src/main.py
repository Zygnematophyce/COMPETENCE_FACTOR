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
        self.title("Skill Factor")
        self.width = 500
        self.height = 550
        self.geometry("{}x{}".format(self.width,
                                     self.height))
    

if __name__ == "__main__":
    print("competence factor")

    # Create a window tkinter object.
    window = MainWindow()

    # Create a Frame.
    main_frame = tk.Frame(window)

    # Create a Canvas.
    main_canvas = tk.Canvas(main_frame,
                            bg="ivory",
                            width=500,
                            height=550)

    # Define the number of skill.
    number_skill = 5
    print("Number of skill : ", number_skill)

    # Define length of main line.
    length_main_line = 210

    # The length of transverse line.
    len_transv_line = 5

    # Centering the origin (default top-left).
    origin_x = window.width/2
    origin_y = length_main_line
    
    # Define the degres.
    degres = 360/number_skill
    print(degres)

    # The degrees to be subtracted from the degree
    # of the main line.
    radian_substract = math.radians(90)

    # Distribution around the circle of lines.
    for i in range(0, number_skill):

        # Define radian.
        radian = math.radians(degres)

        # Adding the points for the main line.
        x_main_line = math.cos(radian)*length_main_line + origin_x
        y_main_line = math.sin(radian)*length_main_line + origin_y

        # Plot main line.
        main_canvas.create_line(origin_x,
                                origin_y,
                                x_main_line,
                                y_main_line)

        # Increment degres
        degres = degres + (360/number_skill)
        print(degres)
    
        # Create 10 transverses lines.
        for y in range(1, 11):
            # Adding all points centered on the main line.
            try:
                point_x_center = ((length_main_line * (10*y) /100) * math.cos(radian)) + origin_x
                point_y_center = ((length_main_line * (10*y) /100) * math.sin(radian)) + origin_y
            except ZeroDivisionError as e:
                print(e)
                point_x_center = origin_x
                point_y_center = origin_y

            # Create the first points of line.
            xa_coord_line = len_transv_line * math.cos(radian - radian_substract) + point_x_center
            ya_coord_line = len_transv_line * math.sin(radian - radian_substract) + point_y_center

            # Create the second points of line.
            xb_coord_line = len_transv_line * -1 * math.cos(radian - radian_substract) + point_x_center
            yb_coord_line = len_transv_line * -1 * math.sin(radian - radian_substract) + point_y_center

            # Plot all transverses lines.
            main_canvas.create_line(xa_coord_line,
                                    ya_coord_line,
                                    xb_coord_line,
                                    yb_coord_line)        

    main_frame.pack()
    main_canvas.pack()

    window.mainloop()
