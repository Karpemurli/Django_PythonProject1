from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm
from .models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    username = request.session.get('username')
    return render(request,'home.html',{'username':username})

def singnup(req):
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(req,'signup.html',{'form':form})


def logout(req):
    req.session.flush()
    req.session.clear()
    return redirect("login")

def login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = User.objects.filter(username=uname,password=pwd).first()
            if user:
                req.session['username'] = uname
                return redirect('home')
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()
    return render(req,'login.html',{'form':form})