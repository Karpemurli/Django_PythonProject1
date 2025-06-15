
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',set_session,name='set_session'),
    path('get/',get_session,name='get_session'),

]
