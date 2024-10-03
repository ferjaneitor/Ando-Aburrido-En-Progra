# Inicializa la lista de inventario
Inventory = []
addItem = True

while addItem:
    # Pide al usuario detalles del artículo
    Item = input("¿Qué artículo te gustaría agregar? (Escribe 'fin' para terminar) ").strip()
    
    # Verifica si el usuario quiere terminar de agregar artículos
    if Item.lower() == 'fin':
        addItem = False
    else:
        try:
            # Obtén el precio y la cantidad del usuario
            Price = float(input("¿Cuál es el precio del artículo? (Escribir con 2 decimales máximo) ").strip())
            Quantity = int(input("¿Cuántos de ese producto te gustaría agregar? ").strip())
            
            # Verifica si el artículo ya existe en el inventario
            item_exists = False
            for entry in Inventory:
                if entry[0] == Item.lower():
                    # Actualiza la cantidad del artículo existente
                    entry[2] += Quantity
                    # Si el precio es diferente, actualízalo
                    if entry[1] != Price:
                        print(f"El precio del artículo '{Item.lower()}' ha cambiado de ${entry[1]:.2f} a ${Price:.2f}.")
                        entry[1] = Price
                    item_exists = True
                    break
            
            # Si el artículo no existe, agrégalo al inventario
            if not item_exists:
                CompleteItemIndex = [Item.lower(), Price, Quantity]
                Inventory.append(CompleteItemIndex)
                print(f"Artículo agregado: {CompleteItemIndex}")
            else:
                print(f"Artículo actualizado: {Item.lower()}, Cantidad: {Quantity}, Precio: ${Price:.2f}")
        
        except ValueError:
            print("Por favor, ingrese un precio y cantidad válidos.")
        
# Imprime el inventario final
print("Inventario final:")
for item in Inventory:
    print(f"Artículo: {item[0]}, Precio: ${item[1]:.2f}, Cantidad: {item[2]}")

# Función para calcular la cantidad total de productos y el valor total
def calculate_totals(inventory):
    total_quantity = 0
    total_value = 0.0
    
    for item in inventory:
        total_quantity += item[2]  # Suma la cantidad del artículo
        total_value += item[1] * item[2]  # Suma el valor total del artículo
    
    return total_quantity, total_value

# Calcula y muestra los totales
total_quantity, total_value = calculate_totals(Inventory)
print(f"\nCantidad total de productos: {total_quantity}")
print(f"Valor total de todos los productos: ${total_value:.2f}")