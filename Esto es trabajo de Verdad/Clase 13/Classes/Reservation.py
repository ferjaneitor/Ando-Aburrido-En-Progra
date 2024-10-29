import re
from datetime import datetime, timedelta

class Reservation:
    def __init__(self, name: str, date: str, time: str, length: str):
        """
        Inicializa una nueva reservación.

        :param name: Nombre de la persona que realiza la reservación.
        :param date: Fecha de la reservación en formato YYYY-MM-DD.
        :param time: Hora de la reservación en formato HH:MM.
        :param length: Duración de la reservación en horas (como string).
        """
        self.name = name
        self.date = date
        self.time = time
        self.length = length

    def validate_date(self, date: str) -> str:
        """Valida el formato de la fecha.

        :param date: Fecha a validar.
        :return: Fecha válida en formato YYYY-MM-DD.
        :raises ValueError: Si el formato es inválido.
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Fecha inválida. Debe estar en formato YYYY-MM-DD.")
    
    def validate_time(self, time: str) -> str:
        """Valida el formato de la hora.

        :param time: Hora a validar.
        :return: Hora válida en formato HH:MM.
        :raises ValueError: Si el formato es inválido.
        """
        if re.match(r'^\d{2}:\d{2}$', time):
            return time
        else:
            raise ValueError("Hora inválida. Debe estar en formato HH:MM.")

    def validate_length(self, length: str) -> int:
        """Valida y convierte la duración a un entero.

        :param length: Duración a validar como string.
        :return: Duración válida como entero.
        :raises ValueError: Si el valor no es un entero positivo.
        """
        try:
            length_int = int(length)
            if length_int <= 0:
                raise ValueError("La duración debe ser un número entero positivo.")
            return length_int
        except ValueError:
            raise ValueError("La duración debe ser un número entero.")

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
    def length(self) -> int:
        """Obtiene la duración de la reservación."""
        return self._length

    @length.setter
    def length(self, value: str):
        """Establece la duración de la reservación después de validarla."""
        self._length = self.validate_length(value)

    def end_time(self) -> str:
        """Calcula la hora de finalización de la reservación.

        :return: Hora de finalización en formato HH:MM.
        """
        start = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        end = start + timedelta(hours=self.length)
        return end.strftime("%H:%M")

    def __str__(self) -> str:
        """Devuelve una representación legible de la reservación.

        :return: Descripción de la reservación.
        """
        return (f"Reservación de {self.name}: {self.date} a las {self.time}, "
                f"duración: {self.length} horas, finaliza a las {self.end_time()}.")
