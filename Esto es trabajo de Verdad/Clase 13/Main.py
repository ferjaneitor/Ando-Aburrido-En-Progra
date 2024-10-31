import re
from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox, ttk
from typing import List
from Classes.Manager import Manager
from Classes.Reservation import Reservation
from datetime import datetime

# Initialize Manager
manager = Manager()  # Initialize the reservation manager

# Functions
def mostrar_fecha_seleccionada(event):
    # Muestra la fecha seleccionada en la consola (opcional).
    fecha = cal.get_date()
    print(f"Fecha seleccionada: {fecha}")

def submit_reservation():
    try:
        name = Name_input.get()
        year = int(year_SpinBox.get())
        month = int(month_SpinBox.get())
        day = int(day_SpinBox.get())
        hour = int(hours_SpinBox1.get())
        minute = int(min_SpinBox1.get())
        length_hours = int(hours_SpinBox2.get())
        length_minutes = int(min_SpinBox2.get())

        # Crear un objeto datetime
        reservation_date = datetime(year, month, day, hour, minute)

        if name:
            # Llamar a add_reservation con los argumentos individuales
            manager.add_reservation(
                name,
                reservation_date.strftime('%Y-%m-%d'),
                reservation_date.strftime('%H:%M'),
                length_hours,
                length_minutes
            )
            update_reservation_table()
            clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")

def update_reservation_table():
    # Actualiza la tabla de reservaciones en la interfaz.
    for item in Reservoir_Table.get_children():
        Reservoir_Table.delete(item)

    # Obtener y mostrar las reservaciones actualizadas
    all_reservations: List[Reservation] = manager.show_all_reservations()
    for reservation in all_reservations:
        data = (reservation.name, reservation.date, reservation.time, reservation.length)
        Reservoir_Table.insert(parent='', index='end', values=data)

def remove_reservation():
    # Elimina la reservación seleccionada.
    selected_item = Reservoir_Table.selection()
    if selected_item:
        name = Reservoir_Table.item(selected_item)['values'][0]
        manager.remove_reservation(name)
        update_reservation_table()
    else:
        messagebox.showwarning("Advertencia", "Seleccione una reservación para eliminar.")

def update_reservation():
    # Actualiza la reservación seleccionada.
    selected_item = Reservoir_Table.selection()
    if selected_item:
        year = int(year_SpinBox.get())
        month = int(month_SpinBox.get())
        day = int(day_SpinBox.get())
        hour = int(hours_SpinBox1.get())
        minute = int(min_SpinBox1.get())
        length_hours = int(hours_SpinBox2.get())
        length_minutes = int(min_SpinBox2.get())
        name = Name_input.get()

        if name:
            date = f"{year}-{month:02}-{day:02}"
            time = f"{hour:02}:{minute:02}"
            length = f"{length_hours}:{length_minutes:02}"

            updated_reservation = Reservation(name, date, time, length)
            old_name = Reservoir_Table.item(selected_item)['values'][0]
            manager.update_reservation(old_name, updated_reservation)
            update_reservation_table()
            clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una reservación para actualizar.")

def clear_entries():
    # Limpia los campos de entrada.
    year_SpinBox.delete(0, tk.END)
    month_SpinBox.delete(0, tk.END)
    day_SpinBox.delete(0, tk.END)
    hours_SpinBox1.delete(0, tk.END)
    min_SpinBox1.delete(0, tk.END)
    hours_SpinBox2.delete(0, tk.END)
    min_SpinBox2.delete(0, tk.END)
    Name_input.delete(0, tk.END)

# Generar la GUI
root = tk.Tk()
root.geometry('1600x800')
root.title('Reservoir Manager')
root.minsize(800, 400)
root.maxsize(1600, 800)

# Emergencia de salida para cerrar
root.bind('<Escape>', lambda event: root.quit())

window = tk.Frame(root)
window.pack(fill=tk.BOTH, expand=True)

# Configuración de la cuadrícula
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(0, weight=1)

# Lado Izquierdo
left_side_Frame = ttk.Frame(window)
left_side_Frame.grid(row=0, column=0, sticky='nsew')

left_side_Frame.rowconfigure(0, weight=1)
left_side_Frame.rowconfigure(1, weight=1)
left_side_Frame.columnconfigure(0, weight=1)

# Calendario
cal : Calendar = Calendar(left_side_Frame, year=2024, month=10, day=29)
cal.grid( row = 0, column = 0, sticky='nsew', padx = 30, pady = 30)

# Lógica
cal.bind("<<CalendarSelected>>", mostrar_fecha_seleccionada)

# Configuración del marco principal
Reservation_input_Frame = ttk.Frame(left_side_Frame, borderwidth=20, relief='groove')
Reservation_input_Frame.grid(row=1, column=0)

# Marco anidado para selector de fecha
date_Frame = ttk.Frame(Reservation_input_Frame)
date_Frame.grid(row=0, column=0, sticky='ew', pady=5)

date_Label = ttk.Label(date_Frame, text='Fecha (YYYY/MM/DD)')
date_Label.grid(row=0, column=0, sticky='nswe')

# SpinBox para el año
year_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=9999, increment=1, width=6)
year_SpinBox.grid(row=0, column=1, sticky='nswe', padx=5, ipadx=10)

ttk.Label(date_Frame, text='/').grid(row=0, column=2, sticky='nswe')

# SpinBox para el mes
month_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=12, increment=1, width=4)
month_SpinBox.grid(row=0, column=3, sticky='nswe', padx=5, ipadx=10)

ttk.Label(date_Frame, text='/').grid(row=0, column=4, sticky='nswe')

# SpinBox para el día
day_SpinBox = ttk.Spinbox(date_Frame, from_=1, to=31, increment=1, width=4)
day_SpinBox.grid(row=0, column=5, sticky='nswe', padx=5, ipadx=10)

# Marco anidado para entrada de nombre
name_Frame = ttk.Frame(Reservation_input_Frame)
name_Frame.grid(row=1, column=0, sticky='ew', pady=5)

Name_Label = ttk.Label(name_Frame, text='Nombre')
Name_Label.grid(row=0, column=0, sticky='nswe', padx=30)

Name_input = ttk.Entry(name_Frame, width=20)
Name_input.grid(row=0, column=1, sticky='nswe', ipadx=36, padx = 10)

# Marco anidado para selector de hora
time_Frame = ttk.Frame(Reservation_input_Frame)
time_Frame.grid(row=2, column=0, sticky='ew', pady=5)

time_Label = ttk.Label(time_Frame, text='Hora (HH : MM)')
time_Label.grid(row=0, column=0, sticky='nswe', padx=31)

# SpinBox para horas
hours_SpinBox1 = ttk.Spinbox(time_Frame, from_=0, to=23, increment=1, width=4)
hours_SpinBox1.grid(row=0, column=1, sticky='nswe', padx=10, ipadx=10)

ttk.Label(time_Frame, text=':').grid(row=0, column=2, sticky='nswe')

# SpinBox para minutos
min_SpinBox1 = ttk.Spinbox(time_Frame, from_=0, to=59, increment=1, width=4)
min_SpinBox1.grid(row=0, column=3, sticky='nswe', padx=10, ipadx=10)

# Marco anidado para selector de duración
length_Frame = ttk.Frame(Reservation_input_Frame)
length_Frame.grid(row=3, column=0, sticky='ew', pady=5)

Length_Label = ttk.Label(length_Frame, text='Duración (HH : MM)')
Length_Label.grid(row=0, column=0, sticky='nswe', padx=20)

# SpinBox para duración en horas
hours_SpinBox2 = ttk.Spinbox(length_Frame, from_=0, to=24, increment=1, width=4)
hours_SpinBox2.grid(row=0, column=1, sticky='nswe', padx=10, ipadx=10)

ttk.Label(length_Frame, text=':').grid(row=0, column=2, sticky='nswe')

# SpinBox para duración en minutos
min_SpinBox2 = ttk.Spinbox(length_Frame, from_=0, to=59, increment=1, width=4)
min_SpinBox2.grid(row=0, column=3, sticky='nswe', padx=10, ipadx=10)

# Botón de envío
submit_button = ttk.Button(Reservation_input_Frame, text="Enviar", command=submit_reservation)
submit_button.grid(row=4, column=0, pady=10, ipadx=50, ipady=10)

# Lado Derecho
right_Side_frame: tk = ttk.Frame(window)
right_Side_frame.grid(row=0, column=1, sticky='nsew')

# Tabla de Reservaciones
Reservoir_Table: tk = ttk.Treeview(right_Side_frame, columns=('Nombre', 'Fecha', 'Hora', 'Duración'), show='headings')
Reservoir_Table.heading('Nombre', text='Nombre')
Reservoir_Table.heading('Fecha', text='Fecha')
Reservoir_Table.heading('Hora', text='Hora')
Reservoir_Table.heading('Duración', text='Duración')
Reservoir_Table.pack(fill='both', expand=True, padx=30, pady=30)

# Población inicial de la tabla
update_reservation_table()

# Evento de selección
def item_selected(event):
    # Rellena los campos de entrada con la reservación seleccionada.
    selected_item = Reservoir_Table.selection()
    if selected_item:
        length = [0,0]
        values = Reservoir_Table.item(selected_item)['values']
        Name_input.delete(0, tk.END)
        Name_input.insert(0, values[0])
        year, month, day = map(int, values[1].split('-'))
        hour, minute = map(int, values[2].split(':'))
        duration_str = values[3]
        match = re.match(r'(\d+)\s*horas\s*(\d+)\s*minutos', duration_str)

        if match:
            length_hours = int(match.group(1))
            length_minutes = int(match.group(2))
            length[0] = length_hours
            length[1] = length_minutes
        else:
            raise ValueError("Formato de duración no válido")

        
        # Establecer SpinBoxes de fecha
        year_SpinBox.delete(0, tk.END)
        year_SpinBox.insert(0, year)
        month_SpinBox.delete(0, tk.END)
        month_SpinBox.insert(0, month)
        day_SpinBox.delete(0, tk.END)
        day_SpinBox.insert(0, day)
        
        # Establecer SpinBoxes de hora
        hours_SpinBox1.delete(0, tk.END)
        hours_SpinBox1.insert(0, hour)
        min_SpinBox1.delete(0, tk.END)
        min_SpinBox1.insert(0, minute)

        # Establecer SpinBoxes de duración
        hours_SpinBox2.delete(0, tk.END)
        hours_SpinBox2.insert(0, length[0])
        min_SpinBox2.delete(0, tk.END)
        min_SpinBox2.insert(0, length[1])

Reservoir_Table.bind('<<TreeviewSelect>>', item_selected)

# Marco para botones
buttons_Frame: tk = ttk.Frame(right_Side_frame)
buttons_Frame.pack(side='bottom')
buttons_Frame.rowconfigure(0, weight=1)
buttons_Frame.columnconfigure(0, weight=1)
buttons_Frame.columnconfigure(1, weight=1)

# Botón de eliminar
remove_Button: tk = ttk.Button(buttons_Frame, text='Eliminar', command=remove_reservation)
remove_Button.grid(row=0, column=0, padx=30, pady=20, sticky='we', ipadx=50, ipady=10)

# Botón de actualizar
update_Button: tk = ttk.Button(buttons_Frame, text='Actualizar', command=update_reservation)
update_Button.grid(row=0, column=1, padx=30, pady=20, sticky='we', ipadx=50, ipady=10)

# Bucle principal de ejecución
root.mainloop()
