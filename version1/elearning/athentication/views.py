from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

def homepage(request):
    return render(request, 'athentication/index.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponse("Login")
    context = {'loginform': form}
    return render(request, 'athentication/my_login.html', context=context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform': form}
    return render(request, 'athentication/register.html', context=context)

def dashboard(request):
    return render(request, 'athentication/dashboard.html')