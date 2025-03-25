from datetime import datetime, timedelta
import json
from typing import List
from .Reservation import Reservation  # Importar la clase Reservation

class Manager:
    def __init__(self, filename: str = 'reservations.json') -> None:
        """
        Inicializa el Manager y carga las reservas desde el archivo JSON.
        
        :param filename: Nombre del archivo JSON donde se almacenan las reservas.
        """
        self.filename = filename  # Asigna el nombre del archivo para almacenar reservas
        self.reservations: List[Reservation] = self._load_reservations()  # Carga las reservas desde el archivo

    def _load_reservations(self) -> List[Reservation]:
        """Carga las reservas desde el archivo JSON."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)  # Carga el contenido del archivo
                # Convierte cada entrada del JSON en un objeto Reservation
                return [
                    Reservation(item['name'], item['date'], item['time'], f"{item['length_hours']}:{item['length_minutes']}")
                    for item in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o hay un error en el formato JSON, crea un nuevo archivo vacío
            with open(self.filename, 'w') as file:
                json.dump([], file)
            return []

    def _save_reservations(self) -> None:
        """Guarda la lista de reservas en el archivo JSON."""
        try:
            with open(self.filename, 'w') as file:
                # Convierte las reservas a diccionarios y las guarda en el archivo
                json.dump([reservation.to_dict() for reservation in self.reservations], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error al guardar las reservas: {e}")

    def add_reservation(self, name: str, date: str, time: str, length_hours: int, length_minutes: int) -> None:
        """Agrega una nueva reserva a la lista.
        
        :param name: Nombre de la persona que hace la reserva.
        :param date: Fecha de la reserva.
        :param time: Hora de la reserva.
        :param length_hours: Duración de la reserva en horas.
        :param length_minutes: Duración de la reserva en minutos.
        """
        length = f"{length_hours}:{length_minutes:02d}"  # Formato correcto para la duración
        reservation = Reservation(name, date, time, length)
        
        # Verifica si ya existe una reserva con el mismo nombre
        if any(r.name == reservation.name for r in self.reservations):
            raise ValueError(f"Ya existe una reserva con el nombre '{reservation.name}'.")
        
        # Verifica la disponibilidad antes de agregar la nueva reserva
        if not self.check_availability(date, time, length_hours, length_minutes):
            raise ValueError("No hay disponibilidad para esta fecha y hora.")
        
        self.reservations.append(reservation)  # Agrega la reserva a la lista
        self._save_reservations()  # Guarda la lista de reservas

    def remove_reservation(self, reservation_name: str) -> None:
        """Elimina una reserva por su nombre.
        
        :param reservation_name: Nombre de la reserva a eliminar.
        """
        # Filtra las reservas, excluyendo la que se quiere eliminar
        self.reservations = [r for r in self.reservations if r.name != reservation_name]
        self._save_reservations()  # Guarda la lista actualizada

    def update_reservation(self, reservation_name: str, updated_reservation: Reservation) -> None:
        """Actualiza una reserva existente.
        
        :param reservation_name: Nombre de la reserva que se va a actualizar.
        :param updated_reservation: Objeto Reservation con la información actualizada.
        """
        for index, reservation in enumerate(self.reservations):
            if reservation.name == reservation_name:
                # Verifica disponibilidad para la nueva reserva
                if not self.check_availability(updated_reservation.date, updated_reservation.time,
                                               updated_reservation.length_hours, updated_reservation.length_minutes,
                                               reservation_name):
                    raise ValueError("No hay disponibilidad para la nueva fecha y hora.")
                
                # Actualiza la reserva y guarda los cambios
                self.reservations[index] = updated_reservation
                self._save_reservations()
                return
        raise ValueError("Reserva no encontrada.")  # Si no se encuentra la reserva

    def check_availability(self, reservation_date: str, reservation_time: str, length_hours: int, length_minutes: int, reservation_name: str = None) -> bool:
        """Verifica si hay disponibilidad para una nueva reserva.
        
        :param reservation_date: Fecha de la reserva.
        :param reservation_time: Hora de la reserva.
        :param length_hours: Duración de la reserva en horas.
        :param length_minutes: Duración de la reserva en minutos.
        :param reservation_name: Nombre de la reserva actual (si se está actualizando).
        :return: True si hay disponibilidad, False en caso contrario.
        """
        reservation_datetime = datetime.strptime(f"{reservation_date} {reservation_time}", "%Y-%m-%d %H:%M")
        end_time = reservation_datetime + timedelta(hours=length_hours, minutes=length_minutes)
        
        for r in self.reservations:
            # Omitir la reserva actual si reservation_name está definido
            if reservation_name and r.name == reservation_name:
                continue
            
            r_start = datetime.strptime(f"{r.date} {r.time}", "%Y-%m-%d %H:%M")
            r_end = r_start + timedelta(hours=r.length_hours, minutes=r.length_minutes)
            
            # Verifica si hay un conflicto de horarios
            if (r.date == reservation_date and (
                (r_start < end_time) and (reservation_datetime < r_end)
            )):
                return False  # Hay un conflicto
        return True  # No hay conflictos

    def show_all_reservations(self) -> List[Reservation]:
        """Devuelve todas las reservas actuales."""
        return self.reservations

    def find_reservation_by_date(self, reservation_date: str) -> List[Reservation]:
        """Busca reservas por fecha.
        
        :param reservation_date: Fecha para buscar reservas.
        :return: Lista de reservas que coinciden con la fecha.
        """
        return [r for r in self.reservations if r.date == reservation_date]

    def find_reservation_by_time(self, reservation_time: str) -> List[Reservation]:
        """Busca reservas por hora.
        
        :param reservation_time: Hora para buscar reservas.
        :return: Lista de reservas que coinciden con la hora.
        """
        return [r for r in self.reservations if r.time == reservation_time]

    def show_menu(self) -> List[str]:
        """Devuelve las opciones del menú como una lista de cadenas."""
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
        """Muestra todas las reservaciones en un formato legible."""
        for reservation in self.reservations:
            print(f"Nombre: {reservation.name}, Fecha: {reservation.date}, Hora: {reservation.time}, "
                  f"Duración: {reservation.length} horas, Fin: {reservation.end_time()}")
