from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todo_list = Todo.objects.all()

    if request.method == 'POST' :
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:todo_list')
    else:
        form = TodoForm()

    if request.method == 'POST' :
        todo_id = request.POST['todo_id']
        todo = get_object_or_404(Todo , id = todo_id)

        if todo.checked:
            todo.checked = False
            todo.save()
        else:
            todo.checked = True
            todo.save()

    return render(request , 'todo.html' , {
        'todo_list' : todo_list ,
        'form' : form,
    })

def update_todo(request , pk):

    todo_id = Todo.objects.get(pk=pk)
    update_form = TodoForm(instance=todo_id)
    if request.method == 'POST' :
        update_form = TodoForm(request.POST , instance=todo_id)
    if update_form.is_valid():
        update_form.save()
        return redirect('home:todo_list')
    else:
        update_form = TodoForm(instance=todo_id)

    return render(request , 'update_todo.html' , {
        'update_form' :update_form,
    })

def todo_delete(request , pk):
    todo_delete = Todo.objects.get(pk=pk)
    todo_delete.delete()
    return redirect('home:todo_list')