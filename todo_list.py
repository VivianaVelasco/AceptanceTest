class Task:
    def __init__(self, nombre, descripcion, prioridad, status="Pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.status = status

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_nombre):
        for task in self.tasks:
            if task.nombre == task_nombre:
                task.status = "Completado"
                break

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
        print("5. Salir")

        eleccion = input("Enter your eleccion: ")

        if eleccion == "1":
            nombre = input("Ingresar el nombre del task: ")
            descripcion = input("Ingresar la descripcion del task: ")
            prioridad = input("Ingresar el task prioritario: ")
            new_task = Task(nombre, descripcion, prioridad)
            todo_manager.add_task(new_task)
            print("Task agregado exitosamente!")

        elif eleccion == "2":
            tasks = todo_manager.list_tasks()
            if not tasks:
                print("Tasks no encontrados.")
            else:
                print("Tasks:")
                for task in tasks:
                    print(f"- {task.nombre} ({task.status})")

        elif eleccion == "3":
            task_nombre = input("Ingresar el task name para marcar como Completado: ")
            todo_manager.mark_task_completed(task_nombre)
            print("Task marcado como Completado.")

        elif eleccion == "4":
            todo_manager.clear_list()
            print("To-do list vacia.")

        elif eleccion == "5":
            print("Existente...")
            break

        else:
            print("Eleccion invalida. Seleccione un numero valido.")
