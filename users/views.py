from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Tutor, Student
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def RegisterOption(request):
    return render(request, "users/register_option.html")

def StudentRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='students')
            user.groups.add(group)

            Student.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/studentregister.html', context)

def TutorRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='colleges')
            user.groups.add(group)

            Tutor.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/tutor_register.html', context)

