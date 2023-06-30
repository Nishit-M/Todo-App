def get_todos(filepath = 'todo.txt'):
      """Read a text file and return a list of todos"""
      with open(filepath, 'r') as file_local:
            todo_local = file_local.readlines()  
      return todo_local

def write_todo(todo_arg,filepath = 'todo.txt'):
      """write a text file"""
      with  open(filepath, 'w') as file:
                  file.writelines(todo_arg)
      


while True:
      prompt = input('Type add or show or edit or complete: ').strip()

      if prompt.startswith('add') or prompt.startswith('new'):
            todo = prompt[4:]
            todo_lst = get_todos()
            todo_lst.append(todo.title()+'\n')        
            write_todo(todo_lst)
            
      elif prompt.startswith('show'):
            todo_lst = get_todos()
            # print(todo_lst)
            for i,j in enumerate(todo_lst):
                  j = j.strip('\n')
                  print(f"{i+1}-{j}")

      elif prompt.startswith('edit'):
            try:
                  ci = int(prompt[4:])
                  todo_lst = get_todos()
                  edited_todo = input('Enter the new todo: ')
                  todo_lst[ci-1] = edited_todo.title()
                  write_todo(todo_lst)
            except:
                  print('Enter valid number')
                  continue

      elif prompt.startswith('break'):
            print('break')
            break

      elif prompt.startswith('complete'):
            completed_todo = int(prompt[9:])
            todo_lst = get_todos()
            todo_lst.pop(completed_todo-1)
            write_todo(todo_lst)

      elif prompt == 'clean':
            with  open('todo.txt', 'w') as file:
                  file.writelines('')

      else:
            print('Hey, you entered an unknown command')
            

