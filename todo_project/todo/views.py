from django.shortcuts import redirect, render

# storage for tasks
tasks = [
    
]

# structure for tasks
class Tasks:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.completed = False

#display the list of task
def todo_list(request):
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

#adding new task
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            task_id = len(tasks) + 1
            tasks.append(Tasks(task_id, task_name))
        return redirect('todo_list')

#deleting task
def delete_task(request, task_id):
    global tasks
    tasks = [task for task in tasks if task.id != int(task_id)] # Filter out the task with the given ID
    return redirect('todo_list')

#completing task
def complete_task(request, task_id):
    global tasks
    for task in tasks:
        if task.id == int(task_id):
            task.completed = True
            break
    return redirect('todo_list')
