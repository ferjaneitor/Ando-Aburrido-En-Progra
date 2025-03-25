import tkinter as tk
from tkinter import ttk

class startScreen (ttk.Frame) :

    def __init__(self):
        super.__init__()
        
        self.label = ttk.Label(text="Hola que hace")
        self.label.pack(pady=20)
