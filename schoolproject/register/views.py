from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from .forms import Form
from .models import Person,Course,Purpose




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "new.html")
        else:
            messages.info(request, "Invalid User")
        return redirect('/register/login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/register/register')
            elif request.POST['username'] == "":
                messages.info(request, "Please Enter Username")
                return redirect('/register/register')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.info(request, 'User created')
            return redirect('/register/login')
        else:
            messages.info(request, 'Password not Matched')
            return redirect('/register/register')
    return render(request, 'register.html')


def new(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/new')
    return render(request, 'home.html')

def purpose(request):
     purpose = request.GET.get(Purpose)
     placeorder = request.get('placeorder')
     if request.method == 'POST':
        if purpose == placeorder:
           messages.info(request, 'Order Confirmed')
     return render(request, "dropdown.html")
