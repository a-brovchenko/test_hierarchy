from django.shortcuts import render, redirect
from .models import Workers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'workers/base.html')

def workers_tree(request):
    node = Workers.objects.all()
    return render(request, 'workers/workers_tree.html', {'nodes':node})

def workers_info(request):
    workers = Workers.objects.all()
    return render(request, 'workers/workers_info.html', {'workers':workers})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

