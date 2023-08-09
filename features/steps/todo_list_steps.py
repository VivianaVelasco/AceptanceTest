from behave import given, when, then
from todo_list import Task, TodoListManager

@given("El to-do list esta vacia")
def step_given_todo_list_empty(contexto):
    contexto.todo_manager = TodoListManager()

@when('El usuario agrega un task "{task_nombre}"')
def step_when_user_adds_task(contexto, task_nombre):
    new_task = Task(task_nombre, "", "")
    contexto.todo_manager.add_task(new_task)

@then('El to-do list contiene "{task_nombre}"')
def step_then_todo_list_contains_task(contexto, task_nombre):
    tasks = [task.nombre for task in contexto.todo_manager.list_tasks()]
    assert task_nombre in tasks

@when("El usuario lista todos los tasks")
def step_when_user_lists_all_tasks(contexto):
    contexto.listed_tasks = contexto.todo_manager.list_tasks()

@then("El output tiene que contener:")
def step_then_output_should_contain(contexto):
    expected_output = contexto.text.strip()
    actual_output = "\n".join([f"- {task.nombre} ({task.status})" for task in contexto.listed_tasks])
    assert expected_output == actual_output

@given("El to-do list contiene tasks:")
def step_given_todo_list_contains_tasks(contexto):
    contexto.todo_manager = TodoListManager()
    for row in contexto.table:
        task = Task(row["Task"], row["Description"], row["Priority"], row["Status"])
        contexto.todo_manager.add_task(task)

@when('El usuario marca task "{task_nombre}" como Completado')
def step_when_user_marks_task_as_completed(contexto, task_nombre):
    contexto.todo_manager.mark_task_completed(task_nombre)

@then('El to-do list tiene que mostrar task "{task_nombre}" como Completado')
def step_then_todo_list_should_show_task_as_completed(contexto, task_nombre):
    tasks = contexto.todo_manager.list_tasks()
    task = next(task for task in tasks if task.nombre == task_nombre)
    assert task.status == "Completado"

@when("el usuario vacia el to-do list")
def step_when_user_clears_todo_list(contexto):
    contexto.todo_manager.clear_list()

@then("El to-do list tiene que estar limpia")
def step_then_todo_list_should_be_empty(contexto):
    tasks = contexto.todo_manager.list_tasks()
    assert len(tasks) == 0
