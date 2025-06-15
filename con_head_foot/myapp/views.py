from django.shortcuts import render,redirect,get_object_or_404
from .editform import EditUserForm,EditContactForm
from .models import Register,Contactpages


# Create your views here.

def Index(request):
    return render(request,'myapp/index.html')

def getHome(request):
    return  render(request,'myapp/home.html')

def getAbout(request):
    return render(request,'myapp/about.html')

def getServices(request):
    return render(request,'myapp/services.html')

def getContact(request):
    users = Contactpages.objects.all()
    return render(request,'myapp/contact.html',{'users':users})

def getRegister(request):
    users = Register.objects.all()
    return render(request,'myapp/register.html',{'users':users})

def submit_register(request):
    if request.method == "POST":
        firstname =request.POST.get("firstname")
        lastname =request.POST.get("lastname")
        address =request.POST.get("address")
        gender =request.POST.get("gender")
        mobile =request.POST.get("mobile")
        password =request.POST.get("password")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        profile_image = request.FILES.get("profile_image")


        register =Register(
            firstname = firstname,
            lastname = lastname,
            address = address,
            gender = gender,
            mobile = mobile,
            password = password,
            country = country,
            state = state,
            city = city,
            profile_image = profile_image,
        )


        try:
            register.save()
            return render(request,"myapp/success.html")
        except:
            return render(request,"myapp/register.html")

    return render(request, "myapp/register.html")



# delete register data


def delete_user(request,user_id):
    users = Register.objects.get(id=user_id)
    users.delete()
    return redirect("register")

# Success Page

def success(request):
    return render(request,'myapp/success.html')




def edit_user(request, user_id):
    user = get_object_or_404(Register, id=user_id)
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'myapp/edit_user.html', {'form': form,'user':user})


def Contactpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        message = request.POST.get("message")


        contact = Contactpages(
            name = name,
            email = email,
            phone = phone,
            location = location,
            message = message

        )

        try:
            contact.save()
            return render(request,"myapp/success.html")
        except:
            return render(request,"myapp/contact.html")

    return render(request,'myapp/contact.html')


def delete_contact(request,contact_id):
    users = Contactpages.objects.get(id=contact_id)
    users.delete()
    return redirect("contact")

def contact_edit(request, contact_id):
    user = get_object_or_404(Contactpages, id=contact_id)
    if request.method == "POST":
        form = EditContactForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    else:
        form = EditContactForm(instance=user)
    return render(request, 'myapp/edit_contact.html', {'form': form, 'user': user})






