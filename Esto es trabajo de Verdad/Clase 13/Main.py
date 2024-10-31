from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from typing import List
from Classes.Manager import Manager
from Classes.Reservation import Reservation

#Funtions

#Calendar
def mostrar_fecha_seleccionada(event):
    fecha = cal.get_date()

def submit_reservation():
    try:
        year = int(year_SpinBox.get())
        month = int(month_SpinBox.get())
        day = int(day_SpinBox.get())
        hour = int(hours_SpinBox1.get())
        minute = int(min_SpinBox1.get())
        # Add validation logic here
        print(f"Reservation for {year}/{month}/{day} at {hour}:{minute} created!")
    except ValueError:
        print("Please enter valid data.")

#Manager
Manager : object = Manager()

#Generamos nuestra GUI
root = tk.Tk()
root.geometry('1600x800')
root.title('Reservoir Manager')
root.minsize(800, 400)
root.maxsize(1600, 800)

# En caso de emergencia escape para salir
root.bind('<Escape>', lambda event: window.quit())

#root.overrideredirect(True)

window = tk.Frame(root)
window.pack(fill=tk.BOTH, expand=True)

#Grid Config
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(0, weight=1)

# # Create a size grip to allow resizing
# grip_nw = ttk.Sizegrip(window)
# grip_nw.place(relx=0.0, rely=0.0, anchor='nw')

# grip_ne = ttk.Sizegrip(window)
# grip_ne.place(relx=1.0, rely=0.0, anchor='ne')

# grip_sw = ttk.Sizegrip(window)
# grip_sw.place(relx=0.0, rely=1.0, anchor='sw')

# grip_se = ttk.Sizegrip(window)
# grip_se.place(relx=1.0, rely=1.0, anchor='se')

#Left Side
left_side_Frame = ttk.Frame(window)
left_side_Frame.grid(row=0, column=0, sticky='nsew')

left_side_Frame.rowconfigure(0, weight=1)
left_side_Frame.rowconfigure(1, weight=1)
left_side_Frame.columnconfigure(0, weight=1)

#Calendar
cal : Calendar = Calendar(left_side_Frame, year=2024, month=10, day=29)
cal.grid( row = 0, column = 0, sticky='nsew', padx = 30, pady = 30)

# Logica
cal.bind("<<CalendarSelected>>", mostrar_fecha_seleccionada)
    
# Main Frame Configuration
Reservation_input_Frame = ttk.Frame(left_side_Frame, borderwidth=20, relief='groove')
Reservation_input_Frame.grid(row=1, column=0)

# Configure rows and columns for uniformity
for i in range(6):
    Reservation_input_Frame.rowconfigure(i, weight=1)
Reservation_input_Frame.columnconfigure(0, weight=1)

# Nested Frame for Date Selector
date_Frame = ttk.Frame(Reservation_input_Frame)
date_Frame.grid(row=0, column=0, sticky='ew', pady=5)

date_Label = ttk.Label(date_Frame, text='Date (YYYY/MM/DD)')
date_Label.grid(row=0, column=0, sticky='nswe')

# Year SpinBox
year_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=9999, increment=1, width=6)
year_SpinBox.grid(row=0, column=1, sticky='nswe', padx=5, ipadx = 10)

ttk.Label(date_Frame, text='/').grid(row=0, column=2, sticky='nswe')
# Month SpinBox
month_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=12, increment=1, width=4)
month_SpinBox.grid(row=0, column=3, sticky='nswe', padx=5, ipadx = 10)

ttk.Label(date_Frame, text='/').grid(row=0, column=4, sticky='nswe')
# Day SpinBox
day_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=31, increment=1, width=4)
day_SpinBox.grid(row=0, column=5, sticky='nswe', padx=5, ipadx = 10)

# Nested Frame for Name Input
name_Frame = ttk.Frame(Reservation_input_Frame)
name_Frame.grid(row=1, column=0, sticky='ew', pady=5,)

Name_Label = ttk.Label(name_Frame, text='Name')
Name_Label.grid(row=0, column=0, sticky='nswe', padx= 26)

Name_input = ttk.Entry(name_Frame, width=20)
Name_input.grid(row=0, column=1, sticky='nswe', ipadx= 14)

# Nested Frame for Time Selector
time_Frame = ttk.Frame(Reservation_input_Frame)
time_Frame.grid(row=2, column=0, sticky='ew', pady=5)

time_Label = ttk.Label(time_Frame, text='Time')
time_Label.grid(row=0, column=0, sticky='nswe', padx= 25)

# Hours SpinBox
hours_SpinBox1 = ttk.Spinbox(time_Frame, from_=1, to=24, increment=1, width=4)
hours_SpinBox1.grid(row=0, column=1, sticky='nswe', padx=10, ipadx = 10)

ttk.Label(time_Frame, text=':').grid(row=0, column=2, sticky='nswe')

# Minutes SpinBox
min_SpinBox1 = ttk.Spinbox(time_Frame, from_=0, to=59, increment=1, width=4)
min_SpinBox1.grid(row=0, column=3, sticky='nswe', padx=10, ipadx = 10)

# Nested Frame for Length Selector
length_Frame = ttk.Frame(Reservation_input_Frame)
length_Frame.grid(row=3, column=0, sticky='ew', pady=5)

Lenght_Label = ttk.Label(length_Frame, text='Length')
Lenght_Label.grid(row=0, column=0, sticky='nswe', padx= 20)

# Hours SpinBox
hours_SpinBox2 = ttk.Spinbox(length_Frame, from_=1, to=24, increment=1, width=4)
hours_SpinBox2.grid(row=0, column=1, sticky='nswe', padx=10, ipadx = 10)

ttk.Label(length_Frame, text=':').grid(row=0, column=2, sticky='nswe')

# Minutes SpinBox
min_SpinBox2 = ttk.Spinbox(length_Frame, from_=0, to=59, increment=1, width=4)
min_SpinBox2.grid(row=0, column=3, sticky='nswe', padx=10, ipadx = 10)

# Submit Button
submit_button = ttk.Button(Reservation_input_Frame, text="Submit")
submit_button.grid(row=4, column=0, pady=10, ipadx = 50, ipady = 10)

#Right Side 

right_Side_frame : tk = ttk.Frame(window)
right_Side_frame.grid(row=0, column=1, sticky='nsew')

#Reservour Table

#GUI
Reservour_Table : tk = ttk.Treeview(right_Side_frame, columns=('Name', 'Date', 'Time', 'Length'), show='headings')
Reservour_Table.heading('Name', text='Name')
Reservour_Table.heading('Date', text='Date')
Reservour_Table.heading('Time', text='Time')
Reservour_Table.heading('Length', text='Length')
Reservour_Table.pack(fill='both',expand = True, padx = 30, pady = 30)

#Logic

all_Reservations: List[Reservation] = Manager.show_all_reservations()

for reservation in all_Reservations:
    Name: str = reservation.name
    Date: str = reservation.date
    Time: str = reservation.time
    Length: str = str(reservation.length)
    Data = (Name, Date, Time, Length)
    Reservour_Table.insert(parent='', index='end', values=Data)

#Events
def item_Selected(_) -> None :
    for items in Reservour_Table.selection():
        print(Reservour_Table.item(items)['values'])

Reservour_Table.bind('<<TreeviewSelect>>', item_Selected)

#Buttons Grid

buttons_Frame : tk = ttk.Frame (right_Side_frame)
buttons_Frame.pack(side = 'bottom')
buttons_Frame.rowconfigure(0, weight=1)
buttons_Frame.columnconfigure(0, weight=1)
buttons_Frame.columnconfigure(1, weight=1)

#Remove Button
remove_Button : tk = ttk.Button(buttons_Frame, text= 'Remove')
remove_Button.grid(row = 0, column = 0, padx = 30, pady = 20, sticky = 'we', ipadx = 50, ipady = 10)

#Update Button
update_Button : tk = ttk.Button(buttons_Frame, text= 'Update')
update_Button.grid(row = 0, column = 1, padx = 30, pady = 20, sticky = 'we', ipadx = 50, ipady = 10)

#Main Run Loop
window.mainloop()