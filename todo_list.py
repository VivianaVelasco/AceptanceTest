class Task:
    def __init__(self, nombre, id, descripcion, prioridad, status="Pendiente"):
        self.nombre = nombre
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.status = status

class TodoListManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1 

    def add_task(self, task):
        task = Task(self.task_counter, task_nombre)
        self.tasks.append(task)
        self.task_counter += 1

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_nombre):
        for task in self.tasks:
            if task.nombre == task_nombre:
                task.status = "Completado"
                break
    
    def delete_task(self, task_id):
        initial_task_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != id]
        updated_task_count = len(self.tasks)


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
            tasks = todo_manager.list_tasks()
            print("Tasks:")
            for task in tasks:
                print({task.id} +" - "+{task.nombre})

            task_id = input("Ingrese el id del task a eliminar: ")
            todo_manager.delete_task(id)

        elif eleccion == "6":
            print("Existente...")
            break

        else:
            print("Eleccion invalida. Seleccione un numero valido.")
