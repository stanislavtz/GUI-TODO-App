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

while True:
    event, values = window.read()
    print("Event: ", event)
    print("Values: ", values)

    if event == sg.WIN_CLOSED:
        break

    if event == "add_todo":
        todo = values["todo"]
        formated_todo = todo.capitalize() + "\n"
        functions.add_todo(FILE_PATH, formated_todo)
        window["todo"].update(value="")

    if event == "show_todo":
        todos_list = functions.get_todos(FILE_PATH)
        if todos_list:
            formatted_todos = functions.display_todos(todos_list)
            window["todos"].update(values=formatted_todos)
        else:
            no_todos = functions.print_no_todos()
            window["todos"].update(no_todos)

    if event == "edit_todo":
        pass


    if event == "complete_todo":
        pass




window.close()