import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('600x800')
window.title('Frames and parenting')

#frame
frame = ttk.Frame(window)
frame.pack()