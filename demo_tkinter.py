"""
Demo of tkinter GUI with examples of many widgets, handlers and so on
"""

import tkinter as tk
import matplotlib.pyplot as plt


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
root = tk.Tk()  # top-level widget, main window of Application
myapp = App(root)

# Method calls to the window manager class
root.title("Demo: tkinter")
root.maxsize(1000, 400)

# start the program
myapp.mainloop()
