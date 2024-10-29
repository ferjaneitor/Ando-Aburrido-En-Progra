import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from typing import List
from Classes.Manager import Manager
from Classes.Reservation import Reservation


class ReservationApp:
    def __init__(self, master):
        self.master = master
        self.manager = Manager()
        self.selected_reservation = None
        
        master.title("Gestión de Reservaciones")
        master.geometry("800x500")

        # Estilo
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TListbox', font=('Arial', 10), padding=5)

        # Menú principal
        self.menu_frame = ttk.Frame(master)
        self.menu_frame.pack(pady=10)

        self.add_button = ttk.Button(self.menu_frame, text="Agregar Reservación", command=self.add_reservation)
        self.add_button.grid(row=0, column=0, padx=5)

        self.remove_button = ttk.Button(self.menu_frame, text="Eliminar Reservación", command=self.remove_reservation)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.update_button = ttk.Button(self.menu_frame, text="Actualizar Reservación", command=self.update_reservation)
        self.update_button.grid(row=0, column=2, padx=5)

        self.check_button = ttk.Button(self.menu_frame, text="Verificar Disponibilidad", command=self.check_availability)
        self.check_button.grid(row=0, column=3, padx=5)

        self.show_button = ttk.Button(self.menu_frame, text="Mostrar Reservaciones", command=self.update_reservation_list)
        self.show_button.grid(row=0, column=4, padx=5)

        # Lista de reservaciones
        self.reservation_listbox = tk.Listbox(master, width=80, height=15)
        self.reservation_listbox.pack(pady=20)
        self.reservation_listbox.bind('<<ListboxSelect>>', self.on_reservation_select)

        # Cuadro de entrada para los detalles de la reservación
        self.detail_frame = ttk.LabelFrame(master, text="Detalles de la Reservación")
        self.detail_frame.pack(pady=10, padx=10, fill="both", expand="yes")

        ttk.Label(self.detail_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.detail_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.detail_frame, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.detail_frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.detail_frame, text="Hora (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.detail_frame)
        self.time_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.detail_frame, text="Duración (horas):").grid(row=3, column=0, padx=5, pady=5)
        self.length_entry = ttk.Entry(self.detail_frame)
        self.length_entry.grid(row=3, column=1, padx=5, pady=5)

    def update_reservation_list(self):
        """Actualiza la lista de reservaciones en la interfaz."""
        self.reservation_listbox.delete(0, tk.END)
        for reservation in self.manager.reservations:
            self.reservation_listbox.insert(tk.END, str(reservation))

    def add_reservation(self):
        """Agrega una nueva reservación usando los datos del cuadro de entrada."""
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        length = self.length_entry.get()

        if name and date and time and length:
            try:
                new_reservation = Reservation(name, date, time, length)
                if self.manager.verify_availability(name):
                    self.manager.add_reservation(new_reservation)
                    self.update_reservation_list()
                    self.clear_entries()
                else:
                    messagebox.showwarning("Error", "La reservación ya existe.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Advertencia", "Complete todos los campos.")

    def remove_reservation(self):
        """Elimina la reservación seleccionada."""
        if self.selected_reservation:
            self.manager.remove_reservation(self.selected_reservation.name)
            self.selected_reservation = None
            self.update_reservation_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una reservación para eliminar.")

    def update_reservation(self):
        """Actualiza la reservación seleccionada usando los datos del cuadro de entrada."""
        if self.selected_reservation:
            name = self.name_entry.get()
            date = self.date_entry.get()
            time = self.time_entry.get()
            length = self.length_entry.get()

            if name and date and time and length:
                try:
                    updated_reservation = Reservation(name, date, time, length)
                    self.manager.update_reservation(self.selected_reservation.name, updated_reservation)
                    self.selected_reservation = updated_reservation
                    self.update_reservation_list()
                    self.clear_entries()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una reservación para actualizar.")

    def check_availability(self):
        """Verifica la disponibilidad de una nueva reservación."""
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if name and date and time:
            if self.manager.verify_availability(name):
                messagebox.showinfo("Disponibilidad", "La reservación está disponible.")
            else:
                messagebox.showwarning("No disponible", "La reservación ya existe.")
        else:
            messagebox.showwarning("Advertencia", "Complete los campos requeridos.")

    def on_reservation_select(self, event):
        """Carga los detalles de la reserva seleccionada en los cuadros de entrada."""
        selection = self.reservation_listbox.curselection()
        if selection:
            self.selected_reservation = self.manager.reservations[selection[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.selected_reservation.name)
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, self.selected_reservation.date)
            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0, self.selected_reservation.time)
            self.length_entry.delete(0, tk.END)
            self.length_entry.insert(0, self.selected_reservation.length)

    def clear_entries(self):
        """Limpia los cuadros de entrada."""
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationApp(root)
    root.mainloop()
