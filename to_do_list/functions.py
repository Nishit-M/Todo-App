def get_todos(filepath = 'todo.txt'):
      """Read a text file and return a list of todos"""
      with open(filepath, 'r') as file_local:
            todo_local = file_local.readlines()  
      return todo_local

def write_todo(todo_arg,filepath = 'todo.txt'):
      """write a text file"""
      with  open(filepath, 'w') as file:
                  file.writelines(todo_arg)