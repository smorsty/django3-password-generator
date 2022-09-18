from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    letters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTYVWXYZ'))

    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))

    if request.GET.get('special'):
        letters.extend(list('!@#$%^&*_+-=,./|;:~'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for j in range(length):
        thepassword += random.choice(letters)

    return render(request, 'generator/password.html', {'password':thepassword})

def info(request):
    return render(request, 'generator/info.html')
