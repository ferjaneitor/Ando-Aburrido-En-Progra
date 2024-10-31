from datetime import datetime
import json
from typing import List
from .Reservation import Reservation # Importar la clase Reservation

class Manager:
    def __init__(self, filename: str = 'reservations.json') -> None:
        
        #Inicializa el Manager y carga las reservas desde el archivo JSON.

        #:param filename: Nombre del archivo donde se guardan las reservaciones.
    
        self.filename = filename
        self.reservations: List[Reservation] = self._load_reservations()
    
    def _load_reservations(self) -> List[Reservation]:
        #Carga las reservas desde un archivo JSON.

        #:return: Lista de objetos Reservation.
        
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Reservation(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.filename, 'w') as file:
                json.dump([], file)
            return []

    def _save_reservations(self) -> None:
        #Guarda la lista de reservas en el archivo JSON.
        try:
            with open(self.filename, 'w') as file:
                json.dump([reservation.to_dict() for reservation in self.reservations], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error al guardar las reservas: {e}")

    def add_reservation(self, reservation: Reservation) -> None:
        #Agrega una nueva reserva a la lista.

        #:param reservation: Objeto Reservation a agregar.
        #:raises ValueError: Si ya existe una reserva con el mismo nombre.
        
        if any(r.name == reservation.name for r in self.reservations):
            raise ValueError(f"Ya existe una reserva con el nombre '{reservation.name}'.")
        if not self.check_availability(reservation.date, reservation.time):
            raise ValueError("No hay disponibilidad para esta fecha y hora.")
        self.reservations.append(reservation)
        self._save_reservations()

    def remove_reservation(self, reservation_name: str) -> None:
        #Elimina una reserva por su nombre.

        #:param reservation_name: Nombre de la reserva a eliminar.
        
        self.reservations = [r for r in self.reservations if r.name != reservation_name]
        self._save_reservations()

    def update_reservation(self, reservation_name: str, updated_reservation: Reservation) -> None:
        #Actualiza una reserva existente.

        #:param reservation_name: Nombre de la reserva a actualizar.
        #:param updated_reservation: Objeto Reservation con la nueva información.
        #:raises ValueError: Si no se encuentra la reserva.
        
        for index, reservation in enumerate(self.reservations):
            if reservation.name == reservation_name:
                self.reservations[index] = updated_reservation
                self._save_reservations()
                return
        raise ValueError("Reserva no encontrada.")

    def check_availability(self, reservation_date: str, reservation_time: str) -> bool:
        #Verifica si hay disponibilidad en la fecha y hora especificadas.

        #:param reservation_date: Fecha de la reserva en formato 'YYYY-MM-DD'.
        #param reservation_time: Hora de la reserva en formato 'HH:MM'.
        #:return: True si hay disponibilidad, False si ya existe una reserva.
        
        reservation_datetime = datetime.strptime(f"{reservation_date} {reservation_time}", "%Y-%m-%d %H:%M")
        return not any(r.date_time == reservation_datetime for r in self.reservations)

    def show_all_reservations(self) -> List[Reservation]:
        #Devuelve todas las reservas actuales.

        #:return: Lista de objetos Reservation.
        
        return self.reservations

    def find_reservation_by_date(self, reservation_date: str) -> List[Reservation]:
        #Busca reservas por fecha.

        #:param reservation_date: Fecha en formato 'YYYY-MM-DD'.
        #:return: Lista de reservas en la fecha especificada.
        
        date_obj = datetime.strptime(reservation_date, "%Y-%m-%d").date()
        return [r for r in self.reservations if r.date_time.date() == date_obj]

    def find_reservation_by_time(self, reservation_time: str) -> List[Reservation]:
        #Busca reservas por hora.

        #:param reservation_time: Hora en formato 'HH:MM'.
        #:return: Lista de reservas a la hora especificada.
        
        time_obj = datetime.strptime(reservation_time, "%H:%M").time()
        return [r for r in self.reservations if r.date_time.time() == time_obj]

    def show_menu(self) -> List[str]:
        #Devuelve las opciones del menú como una lista de cadenas.

        #:return: Lista de opciones del menú.
        
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