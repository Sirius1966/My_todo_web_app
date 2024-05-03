FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Gets the todo_items from the textfile in per default FILEPATH = "todos.txt"
    and returns a list of todo_items.
    :param: filepath: str: FILEPATH = "todos.txt"
    :return: todos_local:list[str]
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg: list, filepath=FILEPATH):
    """
    writes the todos list in the textfile with the FILEPATH = "todos.txt"
    :param filepath: str: FILEPATH = "todos.txt"
    :param todos_arg: list: list of todos
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

