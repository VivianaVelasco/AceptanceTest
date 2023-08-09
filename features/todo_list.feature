Feature: To-Do List Manager

  Scenario: Agregar task al to-do list
    Given el to-do list esta vacia
    When el usuario agrega un task "Buy groceries"
    Then el to-do list tiene que contener "Buy groceries"

  Scenario: Lista todos los tasks en el to-do list
    Given el to-do list contiene tasks:
      | Task        | Description         | Priority |
      | Buy groceries | Buy items for dinner | High     |
      | Pay bills     | Pay utility bills   | Medium   |
    When el usuario listas todos los tasks
    Then el output tiene que contener:
      """
      Tasks:
      - Buy groceries (Pendiente)
      - Pay bills (Pendiente)
      """

  Scenario: Marca un task como Completado
    Given el to-do list contiene tasks:
      | Task          | Description         | Priority | Status   |
      | Buy groceries | Buy items for dinner | High     | Pendiente |
    When el usuario contiene task "Buy groceries" como Completado
    Then el to-do list tiene que mostrar task "Buy groceries" como Completado

  Scenario:Limpiar toda to-do list
    Given el to-do list contiene tasks:
      | Task        | Description         | Priority | Status   |
      | Buy groceries | Buy items for dinner | High     | Pendiente |
      | Pay bills     | Pay utility bills   | Medium   | Pendiente |
    When el usuario vacia el to-do list
    Then el to-do list tiene que estar limpia
