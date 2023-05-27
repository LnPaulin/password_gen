from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Sepcial'):
            characters.extend(list('~!@#$%^&*()__+'))

    if request.GET.get('about'):
        return render(request, 'generator/about.html')

    if request.GET.get('Numbers'):
            characters.extend(list('0123456789'))

    length = int(request.GET.get('Length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    if request.GET.get('home'):
        return render(request, 'generator/home.html')
    return render(request, 'generator/about.html')
