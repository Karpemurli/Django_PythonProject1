from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',singnup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),

]
