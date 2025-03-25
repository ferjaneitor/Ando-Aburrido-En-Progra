Este es un codigo creado en colaboracion de Keyla Aisha Cox Parales y Fernando Joel Cruz Briones

Para que funcione en su totalidad se tendra que instalar lo siguiente:

pip install tkcalendar


Explicaciones echas con ChatGPT con el objetivo de crear documentacion mas que no codigo

---------------------------------------------------------------------------------------------------------------------------------------------

# Sistema de Gestión de Reservas

Este sistema permite gestionar reservas mediante las clases `Manager` y `Reservation`. A continuación, se describen las funciones disponibles y ejemplos de uso.

## Clases

### Manager

La clase `Manager` se encarga de gestionar las reservas, incluyendo la carga y el almacenamiento de datos en un archivo JSON.

#### Métodos

- **`__init__(self, filename: str = 'reservations.json') -> None`**
  - Inicializa el Manager y carga las reservas desde el archivo JSON.
  - **Parámetro:**
    - `filename`: Nombre del archivo JSON (por defecto es 'reservations.json').

- **`_load_reservations(self) -> List[Reservation]`**
  - Carga las reservas desde el archivo JSON y las convierte en objetos `Reservation`.

- **`_save_reservations(self) -> None`**
  - Guarda la lista de reservas actuales en el archivo JSON.

- **`add_reservation(self, name: str, date: str, time: str, length_hours: int, length_minutes: int) -> None`**
  - Agrega una nueva reserva a la lista.
  - **Parámetros:**
    - `name`: Nombre de la persona que hace la reserva.
    - `date`: Fecha de la reserva en formato `YYYY-MM-DD`.
    - `time`: Hora de la reserva en formato `HH:MM`.
    - `length_hours`: Duración de la reserva en horas.
    - `length_minutes`: Duración de la reserva en minutos.
  - **Ejemplo:**
    ```python
    manager.add_reservation("Juan Pérez", "2024-10-31", "14:00", 2, 30)
    ```

- **`remove_reservation(self, reservation_name: str) -> None`**
  - Elimina una reserva por su nombre.
  - **Parámetro:**
    - `reservation_name`: Nombre de la reserva a eliminar.
  - **Ejemplo:**
    ```python
    manager.remove_reservation("Juan Pérez")
    ```

- **`update_reservation(self, reservation_name: str, updated_reservation: Reservation) -> None`**
  - Actualiza una reserva existente.
  - **Parámetros:**
    - `reservation_name`: Nombre de la reserva que se va a actualizar.
    - `updated_reservation`: Objeto `Reservation` con la información actualizada.
  - **Ejemplo:**
    ```python
    updated_res = Reservation("Juan Pérez", "2024-10-31", "15:00", "2:00")
    manager.update_reservation("Juan Pérez", updated_res)
    ```

- **`check_availability(self, reservation_date: str, reservation_time: str, length_hours: int, length_minutes: int, reservation_name: str = None) -> bool`**
  - Verifica si hay disponibilidad para una nueva reserva.
  - **Parámetros:**
    - `reservation_date`: Fecha de la reserva.
    - `reservation_time`: Hora de la reserva.
    - `length_hours`: Duración en horas.
    - `length_minutes`: Duración en minutos.
    - `reservation_name`: Nombre de la reserva actual (opcional, para actualizaciones).
  - **Ejemplo:**
    ```python
    available = manager.check_availability("2024-10-31", "14:00", 2, 30)
    ```

- **`show_all_reservations(self) -> List[Reservation]`**
  - Devuelve todas las reservas actuales.

- **`find_reservation_by_date(self, reservation_date: str) -> List[Reservation]`**
  - Busca reservas por fecha.
  - **Parámetro:**
    - `reservation_date`: Fecha para buscar reservas.
  - **Ejemplo:**
    ```python
    reservas = manager.find_reservation_by_date("2024-10-31")
    ```

- **`find_reservation_by_time(self, reservation_time: str) -> List[Reservation]`**
  - Busca reservas por hora.
  - **Parámetro:**
    - `reservation_time`: Hora para buscar reservas.

- **`show_menu(self) -> List[str]`**
  - Devuelve las opciones del menú como una lista de cadenas.

- **`display_reservations(self) -> None`**
  - Muestra todas las reservas en un formato legible.

---

### Clase Reservation

La clase `Reservation` representa una reserva individual.

#### Métodos y propiedades

- **`__init__(self, name: str, date: str, time: str, length: str)`**
  - Inicializa una nueva reserva.
  - **Parámetros:**
    - `name`: Nombre de la persona que realiza la reserva.
    - `date`: Fecha de la reserva en formato `YYYY-MM-DD`.
    - `time`: Hora de la reserva en formato `HH:MM`.
    - `length`: Duración de la reserva en formato `'horas:minutos'`.

- **`validate_date(self, date: str) -> str`**
  - Valida el formato de la fecha.

- **`validate_time(self, time: str) -> str`**
  - Valida el formato de la hora.

- **`validate_length(self, length: str) -> float`**
  - Valida y convierte la duración de la reserva a horas.

- **Propiedades**:
  - `date`, `time`, `length`, `name`: Aseguran que los datos sean válidos al ser establecidos.

- **`end_time(self) -> str`**
  - Calcula la hora de finalización de la reserva.

- **`to_dict(self) -> dict`**
  - Convierte la reserva a un diccionario para almacenamiento.

---

## Ejemplo de Uso

```python
from Manager import Manager
from Reservation import Reservation

# Crear un Manager
manager = Manager()

# Agregar una reserva
manager.add_reservation("Juan Pérez", "2024-10-31", "14:00", 2, 30)

# Mostrar todas las reservas
manager.display_reservations()

# Buscar por fecha
reservas = manager.find_reservation_by_date("2024-10-31")
