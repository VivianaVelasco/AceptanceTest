from datetime import date
class Task:
    def __init__(self, nombre, prioridad, status="Pendiente", fecha= date.today()):
        self.nombre = nombre
        self.prioridad = prioridad
        self.status = status
        self.fecha = fecha
    
    def mark_task_completed(self):
        self.status = "Completado"
    
    def editar_prioridad(self, prioridad):
        self.prioridad = prioridad

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        i = 0
        print("ID - Nombre - Priority - Status - Date")
        for task in self.tasks:
            print(i, task.nombre, task.prioridad, task.status, task.fecha)
            i += 1

    def mark_task_completed(self, task_nombre):
        for task in self.tasks:
            if task.nombre == task_nombre:
                task.mark_task_completed()
                break
    
    def delete_task(self, task_id):
        del self.tasks[task_id]

    def clear_list(self):
        self.tasks = []

# main
if __name__ == "__main__":
    todo_manager = TodoListManager()

    while True:
        print("\n1. Agregar un task")
        print("2. Listar todos los tasks")
        print("3. Marcar un task como Completado")
        print("4. Limpiar toda to-do list")
        print("5. Eliminar un task especifico del to-do list por id")
        print("6. Salir")

        eleccion = input("Ingrese el numero de tu eleccion: ")

        if eleccion == "1":
            nombre = input("Ingresar el nombre del task: ")
            prioridad = input("Ingresar el task prioritario: ")
            new_task = Task(nombre, prioridad)
            todo_manager.add_task(new_task)
            print("Task agregado exitosamente!")

        elif eleccion == "2":
            todo_manager.list_tasks()

        elif eleccion == "3":
            todo_manager.list_tasks()
            task_nombre = input("Ingresar el task name para marcar como Completado: ")
            todo_manager.mark_task_completed(task_nombre)
            print("Task marcado como Completado.")

        elif eleccion == "4":
            todo_manager.clear_list()
            print("To-do list vacia.")

        elif eleccion == "5":
            todo_manager.list_tasks()
            task_id = int(input("Ingrese el id del task a eliminar: "))
            todo_manager.delete_task(task_id)

        elif eleccion == "6":
            print("App Cerrada")
            break
        else:
            print("Eleccion invalida. Seleccione un numero valido.")