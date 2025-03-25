import re
from datetime import datetime, timedelta

class Reservation:
    def __init__(self, name: str, date: str, time: str, length: str):
        """
        Inicializa una nueva reservación.

        :param name: Nombre de la persona que realiza la reservación.
        :param date: Fecha de la reservación en formato YYYY-MM-DD.
        :param time: Hora de la reservación en formato HH:MM.
        :param length: Duración de la reservación en formato 'horas:minutos'.
        """
        self.name = name          # Asigna el nombre de la reservación
        self.date = date          # Asigna la fecha tras validarla
        self.time = time          # Asigna la hora tras validarla
        self.length = length      # Asigna la duración tras validarla

    def validate_date(self, date: str) -> str:
        """Valida el formato de la fecha."""
        try:
            # Intenta convertir la cadena en un objeto datetime
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Fecha inválida. Debe estar en formato YYYY-MM-DD.")

    def validate_time(self, time: str) -> str:
        """Valida el formato de la hora."""
        if re.match(r'^\d{2}:\d{2}$', time):
            return time
        else:
            raise ValueError("Hora inválida. Debe estar en formato HH:MM.")

    def validate_length(self, length: str) -> float:
        """Valida y convierte la duración de la reservación a horas."""
        try:
            # Divide la cadena en horas y minutos y los convierte a enteros
            hours, minutes = map(int, length.split(':'))
            return hours + minutes / 60.0  # Convertir a horas
        except ValueError:
            raise ValueError("La duración debe estar en el formato 'horas:minutos'.")

    @property
    def date(self) -> str:
        """Obtiene la fecha de la reservación."""
        return self._date

    @date.setter
    def date(self, value: str):
        """Establece la fecha de la reservación después de validarla."""
        self._date = self.validate_date(value)

    @property
    def time(self) -> str:
        """Obtiene la hora de la reservación."""
        return self._time

    @time.setter
    def time(self, value: str):
        """Establece la hora de la reservación después de validarla."""
        self._time = self.validate_time(value)

    @property
    def length(self) -> str:
        """Obtiene la duración de la reservación en formato 'X horas Y minutos'."""
        return f"{self.length_hours} horas {self.length_minutes} minutos"

    @length.setter
    def length(self, value: str):
        """Establece la duración de la reservación a partir de horas y minutos dados."""
        parts = value.split(':')
        if len(parts) != 2:
            raise ValueError("La duración debe estar en el formato 'X:Y'.")
        try:
            # Asigna horas y minutos a las propiedades correspondientes
            self.length_hours = int(parts[0])
            self.length_minutes = int(parts[1])
        except ValueError:
            raise ValueError("La duración debe ser un número entero.")

    @property
    def name(self) -> str:
        """Obtiene el nombre de la reservación."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Establece un nuevo nombre para la reservación."""
        self._name = value

    def end_time(self) -> str:
        """Calcula la hora de finalización de la reserva."""
        # Convierte la fecha y hora de inicio a un objeto datetime
        start_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        # Calcula la hora de finalización sumando la duración
        end_datetime = start_datetime + timedelta(hours=self.length_hours, minutes=self.length_minutes)
        return end_datetime.strftime('%H:%M')  # Devuelve la hora de finalización en formato HH:MM

    def to_dict(self) -> dict:
        """Convierte la reserva a un diccionario para almacenamiento."""
        return {
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'length_hours': self.length_hours,
            'length_minutes': self.length_minutes,
        }
