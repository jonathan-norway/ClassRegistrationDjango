from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
            login(request, user)
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
            return redirect('register')

    context["form"] = UserCreationForm(request.POST)
    return render(request, "signup.html", context)




def register(request):
    return render(request, 'register_classes.html')

def err(request, err):
    context = {'error': err}
    return render(request, "error.html", context)


#require that user is logged in



def show_schedule(request):
    return render(request, "show_registered_classes.html")

def show_class_details(request, classID):
    # if classID doesnt exist, redirect to error with appropriate args.
    context = {classID} #Just to try html
    return render(request, "show_classes.html", context)




def signout(request):
    logout(request)
    return redirect('login')