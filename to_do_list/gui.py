import functions
import PySimpleGUI as gui


label = gui.Text('Type in a todo')
input_box = gui.InputText(tooltip='Enter todo',key='todo')
add_button = gui.Button('Add')



list_box = gui.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button = gui.Button('Edit')

window = gui.Window('My Todo App',layout=[[label],[input_box,add_button],[list_box,edit_button]])
# functions.write_todo()
while True:
    event,values = window.read()
    print(event)
    if event == 'Add':
        print('values')
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todo(todos)
        window['todos'].update(values=todos)
    if event == 'edit':
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo

        functions.write_todo(todos)
        window['todos'].update(values=todos)
    if event == 'todos':
        window['todos'].update(values=values['todos'][0])
    if event == gui.WIN_CLOSED:
        break
    

window.close()


