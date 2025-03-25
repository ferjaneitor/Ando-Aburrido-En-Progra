import tkinter as tk
from tkinter import ttk
from ..screen.startScreen import startScreen

class App (tk.Tk) :
    def __init__(self):
        super().__init__()
        self.title("Restaurant Menu")
        self.geometry("1200x800")

        self.container = startScreen(self)  # Create the instance
        self.container.pack(fill="both", expand=True)  # Make it expand to fill the window
