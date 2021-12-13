from django.shortcuts import render, redirect

def redirect_login(request):
    return redirect("login")



def login(request):
    context = {}
    if(request.method == "GET"):
        return render(request, 'login.html')
    # if user is already registered, redirect to schedule
    # if not, redirect to register


def register(request):
    return render(request, 'register_classes.html')

def err(request, err):
    context = {'error': err}
    return render(request, "error.html", context)


#require that user is logged in
from .models import UserRegisterForm
def signup(request):
    context = {}

    if request.method == "POST":
        user = UserRegisterForm(request.POST)
        user.save()
        return redirect('main:start')

    else:
        context["form"] = UserRegisterForm
    return render(request, "signup.html", context)

def show_schedule(request):
    return render(request, "show_registered_classes.html")

def show_class_details(request, classID):
    # if classID doesnt exist, redirect to error with appropriate args.
    context = {classID} #Just to try html
    return render(request, "show_classes.html", context)