from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from members.forms import SignUpForm

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in"))
            return redirect('list-events')

        else:
            messages.success(request, ("Unable to login! Incorrect username or password. Try again"))
            return redirect('login-user')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out"))
    return redirect("list-events")

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('list-events')
    else:
        form = SignUpForm()

    return render(request, 'authenticate/register.html', {'form':form})