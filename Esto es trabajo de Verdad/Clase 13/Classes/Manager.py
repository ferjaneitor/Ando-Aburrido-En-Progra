from datetime import datetime, timedelta
import json
from typing import List
from .Reservation import Reservation  # Importar la clase Reservation

class Manager:
    def __init__(self, filename: str = 'reservations.json') -> None:
        """Inicializa el Manager y carga las reservas desde el archivo JSON."""
        self.filename = filename
        self.reservations: List[Reservation] = self._load_reservations()
    
    def _load_reservations(self) -> List[Reservation]:
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [
                    Reservation(item['name'], item['date'], item['time'], f"{item['length_hours']}:{item['length_minutes']}")
                    for item in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.filename, 'w') as file:
                json.dump([], file)
            return []

    def _save_reservations(self) -> None:
        """Guarda la lista de reservas en el archivo JSON."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([reservation.to_dict() for reservation in self.reservations], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error al guardar las reservas: {e}")

    def add_reservation(self, name: str, date: str, time: str, length_hours: int, length_minutes: int) -> None:
        """Agrega una nueva reserva a la lista."""
        length = f"{length_hours}:{length_minutes:02d}"  # Formato correcto
        reservation = Reservation(name, date, time, length)
        if any(r.name == reservation.name for r in self.reservations):
            raise ValueError(f"Ya existe una reserva con el nombre '{reservation.name}'.")
        if not self.check_availability(date, time, length_hours, length_minutes):
            raise ValueError("No hay disponibilidad para esta fecha y hora.")
        self.reservations.append(reservation)
        self._save_reservations()


    def remove_reservation(self, reservation_name: str) -> None:
        # Elimina una reserva por su nombre.
        self.reservations = [r for r in self.reservations if r.name != reservation_name]
        self._save_reservations()

    def update_reservation(self, reservation_name: str, updated_reservation: Reservation) -> None:
        # Actualiza una reserva existente.
        for index, reservation in enumerate(self.reservations):
            if reservation.name == reservation_name:
                if not self.check_availability(updated_reservation.date, updated_reservation.time, updated_reservation.length):
                    raise ValueError("No hay disponibilidad para la nueva fecha y hora.")
                self.reservations[index] = updated_reservation
                self._save_reservations()
                return
        raise ValueError("Reserva no encontrada.")

    def check_availability(self, reservation_date: str, reservation_time: str, length_hours: int, length_minutes: int) -> bool:
        """Verifica si hay disponibilidad en la fecha y hora especificadas."""
        reservation_datetime = datetime.strptime(f"{reservation_date} {reservation_time}", "%Y-%m-%d %H:%M")
        end_time = (reservation_datetime + timedelta(hours=length_hours, minutes=length_minutes)).time()
        return not any(
            (r.date == reservation_date and (
                (r.time <= reservation_time < r.end_time()) or
                (reservation_time <= r.time < end_time)
            )) for r in self.reservations
        )
    
    def show_all_reservations(self) -> List[Reservation]:
        """Devuelve todas las reservas actuales."""
        return self.reservations

    def find_reservation_by_date(self, reservation_date: str) -> List[Reservation]:
        # Busca reservas por fecha.
        return [r for r in self.reservations if r.date == reservation_date]

    def find_reservation_by_time(self, reservation_time: str) -> List[Reservation]:
        # Busca reservas por hora.
        return [r for r in self.reservations if r.time == reservation_time]

    def show_menu(self) -> List[str]:
        # Devuelve las opciones del menú como una lista de cadenas.
        return [
            "1. Agregar Reservación",
            "2. Eliminar Reservación",
            "3. Actualizar Reservación",
            "4. Verificar Disponibilidad",
            "5. Mostrar Reservaciones",
            "6. Buscar Reservaciones por Fecha",
            "7. Buscar Reservaciones por Hora",
            "8. Salir"
        ]

    def display_reservations(self) -> None:
        # Muestra todas las reservaciones en un formato legible.
        for reservation in self.reservations:
            print(f"Nombre: {reservation.name}, Fecha: {reservation.date}, Hora: {reservation.time}, "
                  f"Duración: {reservation.length} horas, Fin: {reservation.end_time()}")
