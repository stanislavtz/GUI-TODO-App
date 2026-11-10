import time
import FreeSimpleGUI as sg
from modules import functions

FILE_PATH = "files/todos.txt"

label = sg.Text("Type in a todo")
todo_input = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", key="add_todo")
show_button = sg.Button("Show", key="show_todo")
todos_list = sg.Listbox(values=[], key="todos", size=(40, 5), enable_events=True)
edit_button = sg.Button("Edit", key="edit_todo")
complete_btn = sg.Button("Complete", key="complete_todo")

layout = [
    [label],
    [todo_input, add_button],
    [show_button ],
    [todos_list],
    [edit_button, complete_btn]
]
window = sg.Window("TODO App", layout=layout, font=("Helvetica", 20))

todo_number = 0
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "add_todo":
        todo = values["todo"]
        if todo:
            formated_todo = todo.capitalize() + "\n"
            functions.add_todo(FILE_PATH, formated_todo)
            todos = functions.get_todos(FILE_PATH)
            formated_todos = functions.display_todos(todos)
            window["todos"].update(values=formated_todos)
            window["todo"].update(value="")
        else:
            window["todo"].update(value="Please add some todo here!")

    if event == "show_todo":
        todos_list = functions.get_todos(FILE_PATH)
        if todos_list:
            formatted_todos = functions.display_todos(todos_list)
            window["todos"].update(values=formatted_todos)
        else:
            no_todos = functions.print_no_todos()
            window["todos"].update(no_todos)

    if event == "todos":
        todo_to_edit = values["todos"][0]
        if todo_to_edit:
            data_list = todo_to_edit.split(" - ")
            todo_number = int(data_list[0])
            todo_value = " - ".join(data_list[1:]).strip()
            window["todo"].update(value=todo_value)

    if event == "edit_todo":
        new_todo_value = values["todo"]
        if new_todo_value:
            todos = functions.get_todos(FILE_PATH)
            todos[todo_number - 1] = new_todo_value + "\n"
            functions.save_todos(FILE_PATH, todos)
            formatted_todos = functions.display_todos(todos)
            window["todos"].update(values=formatted_todos)
            window["todo"].update(value="")


    if event == "complete_todo":
        todos = functions.get_todos(FILE_PATH)
        todo_to_complete = todos.pop(todo_number - 1)
        functions.save_todos(FILE_PATH, todos)
        formatted_todos = functions.display_todos(todos)
        window["todos"].update(values=formatted_todos)
        window["todo"].update(value="")

window.close()