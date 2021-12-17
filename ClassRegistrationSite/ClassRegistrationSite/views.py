from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def redirect_login(request):
    return redirect("landingpage")



def userlogin(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('register')
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('landingpage')
        context['error'] = 'User not found!'
    context["form"] = AuthenticationForm()

    return render(request, 'login.html', context)



def signup(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('landingpage')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            my_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, my_user)
            return redirect('landingpage')

    context["form"] = UserCreationForm()
    return render(request, "signup.html", context)



def err(request, err):
    context = {'error': err}
    return render(request, "error.html", context)



def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def landingpage(request):
    context = {}
    context['name'] = request.user.get_username()
    return render(request, 'logged_in_base.html', context)


@login_required(login_url='login')
def register_classes(request):
    return render(request, 'register_classes.html')
    context = {}
    exampleclass = [
        'Intro to Computer Science',
        '1',
        'CISC'
    ]
    context["classes"] = [exampleclass for _ in range(10)]
    return render(request, 'register_classes.html', context)






@login_required(login_url='login')
def show_schedule(request):
    context = {}
    # CINDY
    # get list of classes for user
    user = request.user

    # assign list to variable classList




    #context["classes"] = classList
    return render(request, "show_registered_classes.html", context)



