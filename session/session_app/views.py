from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def set_session(request):
    request.session['username'] = "Murali_Karpe"
    return HttpResponse('Session Data is set: username =Murali_karpe')

def get_session(request):
    username = request.session.get('username','Guest')
    return HttpResponse(f'Session Data:username = {username}')
