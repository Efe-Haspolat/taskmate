from django.http.response import HttpResponse
from django.shortcuts import redirect, render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator#sayfa numaralandırma için
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False) # ders60 adding foreign key  
            instance.manage = request.user # ders60 adding foreign key  
            instance.save() # ders60 adding foreign key 
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        #all_tasks = TaskList.objects.all()
        all_tasks = TaskList.objects.filter(manage=request.user)#yukarıyı böyle yaptık
        paginator = Paginator(all_tasks, 5) #sayfa numaralandırma için
        page = request.GET.get('pg')#sayfa numaralandırma için
        all_tasks = paginator.get_page(page)#sayfa numaralandırma için
        return render(request, 'todolist.html', {'all_tasks':all_tasks} )

@login_required# giriş yapmak gerekir
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:# ders63 güvenlik silme ile ilgili
        task.delete()
    else:
        messages.error(request,("Acces Restricted, You Are Not allowed!"))# ders63 güvenlik silme ile ilgili
    return redirect('todolist')

@login_required # giriş yapmak gerekir
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance = task)#"instance = task" bunu eklemezsek yeni görev oluşturur
        if form.is_valid():
            form.save()
       
        messages.success(request,("Task edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj} )

@login_required # giriş yapmak gerekir
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:# ders63 güvenlik silme ile ilgili
        task.done = True
        task.save()
    else:
        messages.error(request,("Acces Restricted, You Are Not allowed!"))# ders63 güvenlik silme ile ilgili
    return redirect('todolist')

@login_required # giriş yapmak gerekir
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    context = {
        'index_text':'Welcome To Index Page',
        }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        'contact_text':'Welcome To Contact Page',
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':'Welcome To About Page',
        }
    return render(request, 'about.html', context)