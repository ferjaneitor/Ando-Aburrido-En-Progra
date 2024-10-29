Este es un codigo creado en colaboracion de Keyla Aisha Cox Parales y Fernando Joel Cruz Briones

Explicaciones echas con ChatGPT con el objetivo de crear documentacion mas que no codigo

---------------------------------------------------------------------------------------------------------------------------------------------

La clase Reservation se encarga de representar una reserva, incluyendo la validación de los datos y el cálculo de la hora de finalización. Aquí te explico cómo usarla paso a paso:

1. Inicialización
Para crear una nueva reserva, debes instanciar la clase Reservation con los parámetros necesarios: nombre, fecha, hora y duración.

    from .Reservation import Reservation  # Asegúrate de importar la clase

    reserva = Reservation(name="Juan", date="2024-12-01", time="18:00", length="2")

2. Validación de Fecha
Puedes validar la fecha utilizando el método validate_date, aunque al establecer la fecha en el constructor, se valida automáticamente.

    try:
        fecha_valida = reserva.validate_date("2024-12-01")  # Esto no generará error
    except ValueError as e:
        print(e)

3. Validación de Hora
De igual forma, puedes validar la hora usando el método validate_time.

    try:
        hora_valida = reserva.validate_time("18:00")  # Esto no generará error
    except ValueError as e:
        print(e)

4. Validación de Duración
Puedes validar la duración de la reserva usando el método validate_length.

    try:
        duracion_valida = reserva.validate_length("2")  # Esto no generará error
    except ValueError as e:
        print(e)

5. Obtener Hora de Finalización
Una vez que la reserva está creada, puedes calcular la hora de finalización utilizando el método end_time.

    hora_finalizacion = reserva.end_time()
    print(f"La reservación finaliza a las {hora_finalizacion}.")

6. Representación de la Reserva
Si deseas ver una representación legible de la reserva, puedes usar el método __str__.

    print(reserva)  # Esto mostrará la descripción de la reservación

7. Modificar Propiedades
Puedes modificar las propiedades de la reserva, y la validación se realizará automáticamente al utilizar los setters:

    try:
        reserva.date = "2024-12-02"  # Cambiar la fecha
        reserva.time = "19:00"        # Cambiar la hora
        reserva.length = "3"          # Cambiar la duración
    except ValueError as e:
        print(e)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Ejemplo de uso del Manager

La clase Manager se encarga de gestionar reservas, almacenándolas en un archivo JSON y proporcionando métodos para manipularlas. Aquí te explico cómo usarla paso a paso:

1. Inicialización
Para utilizar la clase Manager, primero debes instanciarla. Puedes hacerlo pasando el nombre del archivo JSON donde se guardarán las reservas (por defecto es 'reservations.json'):

    manager = Manager('reservations.json')

2. Agregar Reservaciones
Puedes agregar una nueva reservación creando un objeto de la clase Reservation y llamando al método add_reservation.

    from .Reservation import Reservation  # Asegúrate de importar la clase Reservation

    nueva_reserva = Reservation(name="Juan", date_time="2024-12-01 18:00")  # Cambia los parámetros según la definición de Reservation
    manager.add_reservation(nueva_reserva)

3. Eliminar Reservaciones
Si deseas eliminar una reserva por su nombre, utiliza el método remove_reservation.

    manager.remove_reservation("Juan")

4. Actualizar Reservaciones
Para actualizar una reserva existente, primero debes crear un nuevo objeto Reservation con la información actualizada y luego llamar a update_reservation.

    reserva_actualizada = Reservation(name="Juan", date_time="2024-12-01 19:00")  # Cambia los parámetros según sea necesario
    manager.update_reservation("Juan", reserva_actualizada)

5. Verificar Disponibilidad
Puedes verificar si hay disponibilidad para una fecha y hora específicas usando check_availability.

    disponible = manager.check_availability("2024-12-01", "18:00")
    if disponible:
        print("La fecha y hora están disponibles.")
    else:
        print("Ya existe una reserva en esa fecha y hora.")

6. Mostrar Todas las Reservaciones
Para obtener una lista de todas las reservas actuales, usa el método show_all_reservations.

    reservas = manager.show_all_reservations()
    for reserva in reservas:
        print(reserva)

7. Buscar Reservaciones
Puedes buscar reservas por fecha o por hora utilizando find_reservation_by_date y find_reservation_by_time.

    reservas_fecha = manager.find_reservation_by_date("2024-12-01")
    reservas_hora = manager.find_reservation_by_time("18:00")

    print("Reservas para el 2024-12-01:", reservas_fecha)
    print("Reservas a las 18:00:", reservas_hora)

8. Mostrar Menú
Si necesitas mostrar un menú con las opciones disponibles, puedes llamar a show_menu.

    menu = manager.show_menu()
    for opcion in menu:
        print(opcion)