from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "myapp/index.html")


def Home(request):
    return render(request, "myapp/home.html")

def About(request):
    return render(request, "myapp/about.html")

def Contact(request):
    return render(request, "myapp/contact.html")
