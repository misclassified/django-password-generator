from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'pass_generator/home.html')

def about(request):
    return render(request, 'pass_generator/about.html')

def password(request):

    characters = list('abcdefghilmnopqrstuvz')

    length = int(request.GET.get('length', 6))

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('special'):
        characters.extend(list('./?\|}!@$^&'))


    gen_pas = ''

    for x in range(length):
        gen_pas += random.choice(characters)

    return render(request, 'pass_generator/password.html', {'password': gen_pas})
