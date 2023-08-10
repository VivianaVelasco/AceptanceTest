from behave import given, when, then
from todo_list import Task, TodoListManager

# Add
@given("El to-do list esta vacia")
def step_given_todo_list_empty(contexto):
    contexto.todo_manager = TodoListManager()

@when('el usuario agrega un task {task_nombre}')
def step_when_user_adds_task(contexto, task_nombre):
    new_task = Task(task_nombre, "", "")
    contexto.todo_manager.add_task(new_task)

@then('el to-do list tiene que contener {task_nombre}')
def step_then_todo_list_contains_task(contexto, task_nombre):
    tasks = [str(task) for task in contexto.todo_manager.tasks if task.nombre == task_nombre]
    assert tasks

# List all
@given("el to-do list contiene tasks")
def step_given_todo_list_contains_tasks(contexto):
    contexto.todo_manager = TodoListManager()
    for row in contexto.table:
        task = Task(row["Task"], row["Priority"])
        contexto.todo_manager.add_task(task)

@when("el usuario listas todos los tasks")
def step_when_user_lists_all_tasks(contexto):
    contexto.listed_tasks = contexto.todo_manager.list_tasks()

@then("el output tiene que contener")
def step_then_output_should_contain(contexto):
    for row in contexto.table:
        task = [str(task.nombre) for task in contexto.todo_manager.tasks if task.nombre == row["Task"] and task.prioridad == row["Priority"]]
        assert task

# Marker Task
@when('el usuario contiene task {task_nombre} como Completado')
def step_when_user_marks_task_as_completed(contexto, task_nombre):
    contexto.todo_manager.mark_task_completed(task_nombre)

@then('el to-do list tiene que mostrar task {task_nombre} como Completado')
def step_then_todo_list_should_show_task_as_completed(contexto, task_nombre):
    task = filter(lambda task: task.nombre == task_nombre, contexto.todo_manager.tasks)
    assert task is not None

# Clear
@when("el usuario vacia el to-do list")
def step_when_user_clears_todo_list(contexto):
    contexto.todo_manager.clear_list()

@then("el to-do list tiene que estar limpia")
def step_then_todo_list_should_be_empty(contexto):
    assert len(contexto.todo_manager.tasks) == 0

# Delete
@when('el usuario escribe el task ID for {task_nombre}')
def step_impl(contexto, task_nombre):
    task_index_target = next((index for index, task in enumerate(
        contexto.todo_manager.tasks) if task.nombre == task_nombre), None)
    if task_index_target is not None:
        contexto.todo_manager.tasks.remove(task_index_target)

@then('el task "{task_nombre}" debe estar eliminado del to-do list')
def step_impl(contexto, task_nombre):
    task = [t.nombre for t in contexto.todo_manager.tasks]
    assert task not in contexto.todo_manager.tasks, f"Task '{task_nombre}' sigue existiendo en la lista."