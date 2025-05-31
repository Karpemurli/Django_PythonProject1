from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='root_home'),

    path('index/', Index, name='index'),
    path('home/', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
]
