import os
from datetime import datetime  # Importa el módulo que me dice una hora

#Creo una clase que se encarga de mantener y manejar todos los libros
class BookManager:

    #Es la funcion de inicializacion
    def __init__(self, filename='libros.txt'):
        self.filename = filename
        self.warehouse = []
        self.load_books()

    #Es la funcion encargada de cargar la base de datos de un archivo .txt, lo vamos ahacer apartir de la creacion de un camino existente de nuestro sistema operativo a nuestro script con con el fin de leerlo
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as archivo:
                self.warehouse = [
                    {
                        **dict(zip(["Name", "Description", "Author", "Borrowed", "HourBorrowed"], linea.strip().split(';'))),
                        "Borrowed": prestado == 'True' # type: ignore
                    }
                    for linea in archivo
                ]
            print("Libros cargados desde el archivo.")
        else:
            print("El archivo no existe. Se creará uno nuevo al agregar libros.")

    #Esta funcio se encarga de guardar y actualizar la base de datos para esto nosotros vamos a aabrir el archivo y vamos a escribirle el libro que tiene
    def save_books(self):
        try:
            with open(self.filename, 'w') as archivo:
                for book in self.warehouse:
                    libro_str = f"{book['Name']};{book['Description']};{book['Author']};{book['Borrowed']};{book.get('HourBorrowed', '')}\n"
                    archivo.write(libro_str)
            print("Libros guardados en el archivo.")
        except IOError as e:
            print(f"Error al guardar libros: {e}")

    #Es la funcion encargada de añadir los libros nuevos a nuestra base de datos para ello nosotros agregaremos un diccionario que contendra el nombre, una descriocion, un autor, si esta prestado y a la hora que se presto
    def add_book(self, book_name, description, author):
        self.warehouse.append({"Name": book_name, "Description": description, "Author": author, "Borrowed": False, "HourBorrowed": None})
        self.save_books()
        print(f"El libro '{book_name}' ha sido agregado.")

    #Esta es una funcion encargada de borrar algun libro, nosotros vamos a empezar a iterar dentro de nuestra base de datos hasta encontrar una coindencia apartir de preguntaremos y si es que el usuario decide continuar decidiremos borrarlo
    def delete_book(self, book_name):
        for i, book in enumerate(self.warehouse):
            if book["Name"] == book_name:
                confirm = input(f"¿Estás seguro de que deseas eliminar '{book_name}'? (sí/no): ")
                if confirm.lower() == 'sí':
                    self.warehouse.pop(i)
                    self.save_books()
                    print(f"El libro '{book_name}' ha sido eliminado.")
                return
        print("No se encontró ningún libro con ese nombre.")

    #Es una funcon encargada de mostrar todos los libros que se encuentran adentro por lo que si hay avamos a iterar por cada uno de los elementos para demostrarlos
    def show_warehouse(self):
        if not self.warehouse:
            print("No hay libros en el almacén.")
        else:
            for book in self.warehouse:
                print(f"Nombre: {book['Name']}, Descripción: {book['Description']}, Autor: {book['Author']}, Prestado: {'Sí' if book['Borrowed'] else 'No'}, Hora de préstamo: {book.get('HourBorrowed', 'No determinado')}")

    #Esta es una funcion encargada de buscar coincidencias con la entrada que nostoros le demos ya sea palabras completas o letras, por lo que vamos a iterar por cada uno de los elementos para buscar coincidencias por autor o nombre del libro para despues desplegarlos
    def search_book(self, query):
        if not query:
            print("Por favor, ingresa un término de búsqueda.")
            return
        query = query.lower()
        found = [f"{i+1}.- Nombre: {book['Name']}, Autor: {book['Author']}" for i, book in enumerate(self.warehouse) if query in book["Name"].lower() or query in book["Author"].lower()]
        print("\n".join(found) if found else "No se encontraron libros que coincidan con el término de búsqueda.")

    #Esta funcion nos pertmitira actualizar el contenido que tiene algun libro sin importar si es una descripcion o el autor mas que no el nombre
    def update_book(self, book_name):
        for book in self.warehouse:
            if book["Name"] == book_name:
                field = input("¿Cambiar descripción o autor? (descripcion/autor): ").lower()
                if field in ["descripcion", "autor"]:
                    new_value = input(f"Ingrese el nuevo {field}: ")
                    book[field.capitalize()] = new_value
                    self.save_books()
                    print(f"{field.capitalize()} del libro '{book_name}' ha sido actualizado.")
                else:
                    print("Opción no válida.")
                return
        print("No se encontró ningún libro con ese nombre.")

    #Esta funcion lo que nos permite es prestar un libro asignandole verdadero a que el libro se presto y la hora y fecha del momento que se presto el libro
    def borrow_book(self, book_name):
        for book in self.warehouse:
            if book["Name"] == book_name:
                if not book["Borrowed"]:
                    book["Borrowed"] = True
                    book["HourBorrowed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la hora actual
                    self.save_books()
                    print(f"El libro '{book_name}' ha sido prestado.")
                else:
                    print(f"El libro '{book_name}' ya está prestado.")
                return
        print("No se encontró ningún libro con ese nombre.")

    #Esta funcion nos permite regresas a su estado original y regresar el libro
    def return_book(self, book_name):
        for book in self.warehouse:
            if book["Name"] == book_name:
                if book["Borrowed"]:
                    book["Borrowed"] = False
                    book["HourBorrowed"] = None
                    self.save_books()
                    print(f"El libro '{book_name}' ha sido devuelto.")
                else:
                    print(f"El libro '{book_name}' no está prestado.")
                return
        print("No se encontró ningún libro con ese nombre.")

    def show_menu(self):
        options = [
            "1. Agregar libro",
            "2. Borrar libro",
            "3. Mostrar almacén",
            "4. Buscar libro",
            "5. Actualizar libro",
            "6. Prestar libro",
            "7. Devolver libro",
            "8. Salir"
        ]
        print("Menú de opciones:\n" + "\n".join(options))

#Cremos nuestro objeto
manager = BookManager()

#Creamos nuestra funcion main donde contendra todo y llamamos a las funciones que se encuentran adentro de nuestro objeto
def main():
    while True:
        manager.show_menu()
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            manager.add_book(input("Nombre del libro: "), input("Descripción: "), input("Autor: "))
        elif choice == '2':
            manager.delete_book(input("Nombre del libro a borrar: "))
        elif choice == '3':
            manager.show_warehouse()
        elif choice == '4':
            manager.search_book(input("Ingresa término para buscar: "))
        elif choice == '5':
            manager.update_book(input("Nombre del libro a actualizar: "))
        elif choice == '6':
            manager.borrow_book(input("Nombre del libro a prestar: "))
        elif choice == '7':
            manager.return_book(input("Nombre del libro a devolver: "))
        elif choice == '8':
            break
        else:
            print("Opción no válida.")
        
        print("")
        print("-------------------------------------------------------------------------------------------")
        print("")

if __name__ == "__main__":
    main()