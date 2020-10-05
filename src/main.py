# coding: utf-8

"""
Author: Zygnematophyce
Based on radar chart from : https://en.wikipedia.org/wiki/Radar_chart
create a custom to do list with skill graphical view.
"""

import tkinter as tk
import math
import random


class RootWindow(tk.Tk):
    """ Create the main window. """

    def __init__(self):
        super(RootWindow, self).__init__()
        self.title("Skill Factor")
        self.width = 500
        self.height = 550
        self.geometry("{}x{}".format(self.width,
                                     self.height))


class RadarChart(tk.Frame):
    """ Class for radar chart draw by a canvas. """

    def __init__(self, master, number_skill=1):
        super(RadarChart, self).__init__(master)
        self.number_skill = number_skill
        self.master = master

        # Background color of canvas.
        self.background_color = "ivory"

        # The width and height of canvas.
        self.width = self.master.width
        self.heigth = 500
        
        # Create the canvas object.
        self.canvas = tk.Canvas(self,
                                bg=self.background_color,
                                width=self.width,
                                height=self.heigth)

        # Length of main line.
        self.length_main_line = 210
        
        # Length of transverse line.
        self.length_tiny_line = 5

        # Centering the origin (default top-left).
        self.origin_x = self.master.width/2
        self.origin_y = self.length_main_line
        
        # defines the number of degrees according to the
        # number of skills.
        self.degres = 360/number_skill

        # Create the radar chart.
        self.draw_radar_chart(self.canvas)

        # Test draw polygon.
        self.draw_polygon(self.canvas)
        
        # Pack canvas and frame objects.
        self.canvas.pack()
        self.pack()


        """ Function to draw the radar chart object. """
        
    def draw_radar_chart(self, canvas):
        # The degrees to be subtracted from the degree
        # of the main line.
        radian_substract = math.radians(90)

        # Define color of radar chart.
        color_line = "#999999"
        
        # Distribution around the circle of lines.
        for i in range(0, self.number_skill):

            # Define radian.
            radian = math.radians(self.degres)

            # Adding the points for the main line.
            x_main_line = math.cos(radian) * self.length_main_line + self.origin_x
            y_main_line = math.sin(radian) * self.length_main_line + self.origin_y

            # Plot main line.
            canvas.create_line(self.origin_x,
                               self.origin_y,
                               x_main_line,
                               y_main_line,
                               fill=color_line)

            # Increment degres.
            self.degres = self.degres + (360/self.number_skill)

            # Create 10 transverses lines.
            for y in range(1, 11):
                
                # Adding all points centered on the main line.
                try:
                    point_x_center = ((self.length_main_line * (10*y) /100) * math.cos(radian)) + self.origin_x
                    point_y_center = ((self.length_main_line * (10*y) /100) * math.sin(radian)) + self.origin_y
                except ZeroDivisionError as e:
                    print(e)
                    point_x_center = self.origin_x
                    point_y_center = self.origin_y

                # Create the first points of line.
                xa_coord_line = self.length_tiny_line * math.cos(radian - radian_substract) + point_x_center
                ya_coord_line = self.length_tiny_line * math.sin(radian - radian_substract) + point_y_center

                # Create the second points of line.
                xb_coord_line = self.length_tiny_line * -1 * math.cos(radian - radian_substract) + point_x_center
                yb_coord_line = self.length_tiny_line * -1 * math.sin(radian - radian_substract) + point_y_center

                # Plot all transverses lines.
                canvas.create_line(xa_coord_line,
                                   ya_coord_line,
                                   xb_coord_line,
                                   yb_coord_line,
                                   fill=color_line)        


    def draw_polygon(self, canvas):
        
        # List with all coordinates of polygon.
        coord_polygon_list = list()

        # Color line of polygon.
        color_line = "#666666"
        
        # Distribution around the circle of lines.
        for i in range(0, self.number_skill):
            
            # Define radian.
            radian = math.radians(self.degres)

            # Random skill value.
            skill_rank = random.randint(0, 10)

            polygon_x = ((self.length_main_line * (10*skill_rank) /100) * math.cos(radian)) + self.origin_x
            polygon_y = ((self.length_main_line * (10*skill_rank) /100) * math.sin(radian)) + self.origin_y

            coord_polygon_list.extend([polygon_x, polygon_y])

            # Increment degres.
            self.degres = self.degres + (360/self.number_skill)
        
        # Plot simple polygon for test.
        canvas.create_polygon(coord_polygon_list,
                              outline=color_line,
                              fill="",
                              width=5)
                              

class Polygon(tk.Frame):
    """ Class to draw the polygon  """

    def __init__(self, master):
        super(Polygon, self).__init__(master)

        # Pack canvas and frame objects.
        self.canvas.pack()
        self.pack()


if __name__ == "__main__":
    print("competence factor")

    # Create a window tkinter object.
    root_window = RootWindow()
    
    # Define the number of skill.
    SKILL = 5
    print("Number of skill : ", SKILL)

    # Create the radarchart.
    draw_radarchart = RadarChart(root_window, SKILL)

    # Create the irregular polygon line.

    # Create the skill to-do list.
    check_button = tk.Checkbutton(root_window,
                                  text="hello world",
                                  onvalue="hello world",
                                  offvalue="",
                                  anchor="s",
                                  width=20)

    check_button.pack()

    root_window.mainloop()
