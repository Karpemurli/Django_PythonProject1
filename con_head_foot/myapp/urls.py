from django.urls import path
from .views import *

urlpatterns = [

    path('', getHome, name='root_home'),
    path('index', Index, name='index'),
    path('home/', getHome, name="home"),
    path('about/', getAbout, name="about"),
    path('services/', getServices, name='services'),
    path('contact/', getContact, name="contact"),
    path('register/', getRegister, name="register"),
    path('submit_register/', submit_register, name="submit_register"),
    path('edit/<int:user_id>', edit_user, name="edit_user"),
    path('delete_user/<int:user_id>', delete_user, name="delete_user"),
    path('success/', success, name="success"),
    path('Contactpage/', Contactpage, name="Contactpage"),
    path('delete_contact/<int:contact_id>',delete_contact,name="delete_contact"),
    path('contact_edit/<int:contact_id>',contact_edit,name="contact_edit"),

]
