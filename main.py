import FreeSimpleGUI as sg

FILE_PATH = "files/todos.txt"

label = sg.Text("Type in a todo")
todo_input = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

layout = [
    [label],
    [todo_input, add_button],
]

window = sg.Window("TODO App", layout=layout, font=("Helvetica", 20))
window.read()
window.close()