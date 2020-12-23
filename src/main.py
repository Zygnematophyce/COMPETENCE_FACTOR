# coding: utf-8

"""
Author: Zygnematophyce
Based on radar chart from : https://en.wikipedia.org/wiki/Radar_chart
create a custom to do list with skill graphical view.

All material design from : https://material.io/resources/icons/
"""

import tkinter as tk
from tkinter import messagebox
import math
import random


class App(tk.Tk):
    """ Create the main window. """

    def __init__(self):
        super(App, self).__init__()
        self.title("Skill Factor")
        self.width = 925
        self.height = 700
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
        self.width_canvas = 500
        self.heigth_canvas = 500

        # Create the canvas object.
        self.canvas = tk.Canvas(self,
                                bg=self.background_color,
                                width=self.width_canvas,
                                height=self.heigth_canvas)

        # Length of main line.
        self.length_main_line = 210

        # Length of transverse line.
        self.length_tiny_line = 5

        # Centering the origin (default top-left).
        self.origin_x = self.width_canvas/2
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
        self.grid(row=0, column=0, sticky=tk.W)

    def draw_radar_chart(self, canvas):
        """ Function to draw the radar chart object. """

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
            x_main_line = math.cos(radian) * self.length_main_line \
                + self.origin_x
            y_main_line = math.sin(radian) * self.length_main_line \
                + self.origin_y

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
                    point_x_center = ((self.length_main_line * (10*y) / 100)
                                      * math.cos(radian)) + self.origin_x
                    point_y_center = ((self.length_main_line * (10*y) / 100)
                                      * math.sin(radian)) + self.origin_y
                except ZeroDivisionError as e:
                    print(e)
                    point_x_center = self.origin_x
                    point_y_center = self.origin_y

                # Create the first points of line.
                xa_coord_line = self.length_tiny_line * \
                    math.cos(radian - radian_substract) + point_x_center
                ya_coord_line = self.length_tiny_line * \
                    math.sin(radian - radian_substract) + point_y_center

                # Create the second points of line.
                xb_coord_line = self.length_tiny_line \
                    * -1 * math.cos(radian - radian_substract) + point_x_center
                yb_coord_line = self.length_tiny_line \
                    * -1 * math.sin(radian - radian_substract) + point_y_center

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

            polygon_x = ((self.length_main_line * (10*skill_rank) / 100)
                         * math.cos(radian)) + self.origin_x
            polygon_y = ((self.length_main_line * (10*skill_rank) / 100)
                         * math.sin(radian)) + self.origin_y

            coord_polygon_list.extend([polygon_x, polygon_y])

            # Increment degres.
            self.degres = self.degres + (360/self.number_skill)

        # Plot simple polygon for test.
        canvas.create_polygon(coord_polygon_list,
                              outline=color_line,
                              fill="",
                              width=5)


class SkillBox(tk.Frame):
    """ Class with all skill. """

    def __init__(self, master):
        super(SkillBox, self).__init__(master)
        self.master = master

        self.labelframe_skill = tk.LabelFrame(self.master,
                                              text="skill frame")

        # Create text associed with entry.
        self.entry_text = tk.StringVar()

        # Create a Label.
        self.list_skill_label = list()
        self.column_skill = 1

        # Create a button to add skill.
        self.btn_root_skill = tk.Button(self.labelframe_skill,
                                        compound=tk.CENTER,
                                        relief=tk.FLAT,
                                        command=lambda:
                                        self.__add_root_skill(self.entry_text,
                                                              self.column_skill))

        # Create a Entry
        self.entry_root_skill = tk.Entry(self.labelframe_skill,
                                         width=55,
                                         textvariable=self.entry_text)

        self.btn_root_skill.grid(row=0, column=0)
        self.entry_root_skill.grid(row=0, column=1)
        self.labelframe_skill.grid(row=1, column=0)
        self.grid(row=1, column=0)

    def __add_root_skill(self, text, column_skill):
        """ Private function to add root skill. """

        # Recover the text from entry box.
        skill_text = text.get()

        # Warning when nothing is written.
        if len(skill_text.strip()) == 0:
            tk.messagebox.showerror(title="No skill",
                                    message="Nothing is written")
        else:

            # Add new column for each skill.
            column_skill = column_skill + 1

            # Create a label wiht skill.
            skill_Label = tk.Label(self.labelframe_skill)

            # Add label.
            skill_Label.config(text=skill_text)
            skill_Label.grid(row=self.column_skill, column=1)

            # Add to list of label.
            self.list_skill_label.append(skill_Label)

            # Update column_skill
            self.column_skill = column_skill


class TodoListSkill(tk.Frame):
    """ Class for todolist of specific skill. """

    def __init__(self, master):
        super(TodoListSkill, self).__init__(master)
        self.master = master

        self.labelframe_todolist = tk.LabelFrame(self.master,
                                                 text="<<skill>>",
                                                 width=400,
                                                 height=300)
        self.label_todolist = tk.Label(self.labelframe_todolist,
                                       text="test skill")

        self.labelframe_todolist.grid(row=0, column=1, padx=10)


if __name__ == "__main__":
    print("Skill factor")

    # Create a window tkinter object.
    root_window = App()

    # Define the number of skill.
    SKILL = 5
    print("Number of skill : ", SKILL)

    # Create the radarchart.
    draw_radarchart = RadarChart(root_window, SKILL)

    # Create a skill part.
    skill_box = SkillBox(root_window)

    # Create a todolist part.
    todo_list = TodoListSkill(root_window)

    root_window.mainloop()
