from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUserModel, Task, Tag
from .forms import CustomUserCreationForm, TaskForm

def index(request):
    """
    Welcome page of application
    Describes functionality of app
    Allows user to log in/sign up
    """
    return render(request, 'tasks/index.html')

def sign_up(request):
    """
    Allow users to sign up
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    """
    Allow users to log into the application
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'log_in.html', {'form':form})

@login_required
def dashboard(request):
    """
    User dashboard
    """
    user = request.user
    return render(request, 'dashboard.html', {'user':user})

def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')

@login_required
def add_task(request):
    """
    View for adding a task. Upon creation of task, user is redirected to 
    their dashboard with a success message
    """
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added!')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'user':user, 'form':form})

def task_list(request):
    """
    View function for listing all tasks.
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail():
    pass


