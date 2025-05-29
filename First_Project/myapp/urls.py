from django.urls import path
from .views import *

urlpatterns = [
    path('', First, name='First'),
]
