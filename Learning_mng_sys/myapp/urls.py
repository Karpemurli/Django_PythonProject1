from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', Home, name='root_home'),
=======
>>>>>>> 4bdc81c (update)

    path('index/', Index, name='index'),
    path('home/', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
]
