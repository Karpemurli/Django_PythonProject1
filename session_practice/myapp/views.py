from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from .models import User
from django.http import HttpResponse

# Create your views here.


def home(request):
    username = request.session.get('username')
    return render(request,'myapp/home.html',{'username':username})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('login')
    else:
        form = SignUpForm()
    return render(request,'myapp/signup.html',{'form':form})


def logout(request):
    request.session.flush()
    request.session.clear()

    return redirect('login')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = User.objects.filter(username=uname,password=pwd).first()
            if user:
                request.session['username'] = uname
                return redirect('home')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request,'myapp/login.html',{'form':form})

