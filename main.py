import time
import FreeSimpleGUI as sg
from modules import functions

FILE_PATH = "files/todos.txt"

sg.theme("DarkTeal12")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a todo")
todo_input = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", key="add_todo")
show_button = sg.Button("Show", key="show_todo")
todos_list = sg.Listbox(values=[],
                        key="todos",
                        size=(40, 5),
                        enable_events=True,)
edit_button = sg.Button("Edit", key="edit_todo")
complete_btn = sg.Button("Complete", key="complete_todo")
exit_button = sg.Button("Exit", key="exit")

window = sg.Window("TODO App",
                   layout=[[clock],
                           [label],
                           [todo_input, add_button],
                           [show_button],
                           [todos_list],
                           [edit_button, complete_btn,exit_button]],
                   font=("Helvetica", 20))

todo_number = 0

while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    window["clock"].update(value=time.strftime("%d-%b-%Y %H:%M:%S"))

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
            sg.popup("Please write some todo!", title="Invalid Input", font=("Helvetica", 20))

    if event == "show_todo":
        todos_list = functions.get_todos(FILE_PATH)
        if todos_list:
            formatted_todos = functions.display_todos(todos_list)
            window["todos"].update(values=formatted_todos)
        else:
            no_todos = functions.print_no_todos()
            sg.popup(no_todos, title="No Todos", font=("Helvetica", 20))

    if event == "todos":
        try:
            todo_to_edit = values["todos"][0]
            data_list = todo_to_edit.split(" - ")
            todo_number = int(data_list[0])
            todo_value = " - ".join(data_list[1:]).strip()
            window["todo"].update(value=todo_value)
        except IndexError:
            sg.popup("Please select some todo.", title="Invalid Action", font=("Helvetica", 20))

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

    if event == "exit":
        break

window.close()