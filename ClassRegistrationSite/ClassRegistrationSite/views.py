from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def redirect_login(request):
    return redirect("login")



def login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('register')
    if(request.method == "POST"):
        user = authenticate(request.POST["username"], request.POST["password"])
        if user is not None:
            login(user)
            return redirect('register')

    context["form"] = AuthenticationForm

    return render(request, 'login.html', context)



def signup(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('register')

    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            login(request, user)
            return redirect('landing')

    context["form"] = UserCreationForm(request.POST)
    return render(request, "signup.html", context)



def err(request, err):
    context = {'error': err}
    return render(request, "error.html", context)



def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def landingpage(request):
    return render(request, 'logged_in_base.html')


@login_required(login_url='login')
def register_classes(request):
    return render(request, 'register_classes.html')





@login_required(login_url='login')
def show_schedule(request):
    return render(request, "show_registered_classes.html")



