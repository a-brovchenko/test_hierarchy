from django.shortcuts import render, redirect
from .models import Workers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    return render(request, 'workers/base.html')


def workers_tree(request):
    nodes = Workers.objects.all()
    return render(request, 'workers/workers_tree.html', {'nodes':nodes})


def load_workers_level(request):
    if request.method == 'POST':
        parent_id = request.POST.get('data')
        workers = list(Workers.objects.filter(parent_id=parent_id).values())
        return JsonResponse({'workers': workers})
        


def workers_info(request):
    workers = Workers.objects.all()
    return render(request, 'workers/workers_info.html', {'workers':workers})


def sort_table(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data in ('name', 'position', 'email', 'employment_date'):
            workers = list(Workers.objects.order_by(data).values())
        else:
            workers = list(Workers.objects.filter(
                Q(name=data) |
                Q(position=data) |
                Q(email=data) 
            ).values())
    return JsonResponse({'workers': workers})


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

