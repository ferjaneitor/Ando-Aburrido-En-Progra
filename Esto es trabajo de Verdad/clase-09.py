tasks = []

def main():
    programRunning = True
    while programRunning:
        showMenu()
        try:
            task2Do = int(input("Ingresa aqui el numero: "))
            if task2Do == 1:
                addTask()
            elif task2Do == 2:
                removeTask()
            elif task2Do == 3:
                checkTask()
            elif task2Do == 4:
                showTaskList()
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Ingrese un valor válido")

def showMenu():
    print("Ingresa un numero para seleccionar que quieres hacer:")
    print("1. Agregar una tarea")
    print("2. Remover una tarea")
    print("3. Marcar como completada una tarea")
    print("4. Mostrar todas las tareas")
    print("------------------------------------------------------------")

def addTask():
    task = input("Ingresa la tarea: ")
    tasks.append({'task': task, 'completed': False})
    print(f"Tarea '{task}' agregada.")

def removeTask():
    showTaskList()
    try:
        taskNumber = int(input("Ingresa el número de la tarea a remover: ")) - 1
        if 0 <= taskNumber < len(tasks):
            removed_task = tasks.pop(taskNumber)
            print(f"Tarea '{removed_task['task']}' removida.")
        else:
            print("Número de tarea inválido.")
    except (ValueError, IndexError):
        print("Ingrese un número válido.")

def checkTask():
    showTaskList()
    try:
        taskNumber = int(input("Ingresa el número de la tarea a marcar como completada: ")) - 1
        if 0 <= taskNumber < len(tasks):
            tasks[taskNumber]['completed'] = True
            print(f"Tarea '{tasks[taskNumber]['task']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except (ValueError, IndexError):
        print("Ingrese un número válido.")

def showTaskList():
    if not tasks:
        print("No hay tareas en la lista.")
        return
    print("Lista de tareas:")
    for index, task in enumerate(tasks):
        status = "✔️ Completada" if task['completed'] else "❌ Pendiente"
        print(f"{index + 1}. {task['task']} - {status}")

if __name__ == "__main__":
    main()
