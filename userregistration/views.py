from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.


def home(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()
            messages.success(request, "Created Successfully!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {'form':form})

