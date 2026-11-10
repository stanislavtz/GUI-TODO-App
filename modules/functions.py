def get_todos(file_path):
    """
    Reads all the todos from a file and returns a list of todos.
    If the file not exist it prints "File Not Found" and returns an empty list.
    """
    try:
        with open(file_path, "r") as file:
            todos_list = file.readlines()
        return todos_list
    except FileNotFoundError:
        print("File Not Found!")
        return []


def add_todo(file_path, todo_to_add):
    """ Adds new task and save it in the file. """
    with open(file_path, "a") as file:
        file.write(todo_to_add.capitalize())


def display_todos(todos_list):
    """ Reads all the todos from a file and displays them on the screen. """
    formatted_todos = [f"{index+1} - {todo}" for index, todo in enumerate(todos_list)]
    return formatted_todos


def save_todos(file_path, todos_list):
    """ Saves all the todos in the file. """
    with open(file_path, "w") as file:
        file.writelines(todos_list)


def print_no_todos():
    """ Prints \"No todos available.\" """
    return "No todos available!"