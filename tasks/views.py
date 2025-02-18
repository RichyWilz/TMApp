from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task
from accounts.models import User
from .forms import TaskCreationForm
from .tasks import send_email_task
from django.views import View

@login_required
def dashboard(request):
    # task = get_object_or_404(Task,id)
    context = {}
   
    if request.method == 'GET':
        if not request.user.role:
            messages.error(request, 'You do not have a role assigned. Please contact the admin.')
            tasks = []
        else:

            tasks = Task.objects.all() if request.user.role.name.lower() in ['task manager', 'admin'] else Task.objects.filter(assigned_to=request.user)
            
            context['tasks'] = tasks
            task_form = TaskCreationForm()

            context['task_form'] = task_form

    
    if request.method == 'POST':
        if 'task_form_submitted' in request.POST:
            form = TaskCreationForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                user = get_object_or_404(User, id=task.assigned_to.id)
                task.save()

                if user.email:
                   subject = 'New Task Assigned'
                   message = f'A good day to you. \n\n This is to inform you that a new task {task.name} has been assigned to you. Please login to the TMApp to see more details. \n Regards,\n{request.user.name}.'
                   try:
                       send_email_task(subject,user.email,message)
                   except:
                        pass
                    
                messages.success(request, 'Task Added Successfully.')
                return redirect('home')
            else:
                messages.error(request, 'There was an error creating the task, please try again.')
                # return redirect('dashboard')
            
    return render(request, 'dashboard.html', context=context)


class update_task(LoginRequiredMixin, View):
    def get(self, request, slug):
        task = get_object_or_404(Task, slug=slug)
        form = TaskCreationForm(instance=task)
        return render(request, 'update_task.html', {'form':form})
    
    def post(self, request, slug):
        task = get_object_or_404(Task, slug=slug)
        form = TaskCreationForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error updating the task.')
            return redirect('home')
        

class mark_task_completed(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()

        messages.success(request, 'Task labelled complete successfully.')
        return redirect('home')
    
@login_required
def delete_task(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('home')