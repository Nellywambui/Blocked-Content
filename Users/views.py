from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def Login (request):
    return render(request, 'Login.html')


def Register (request):
    return render(request, 'Register.html')


def Gallery (request):
    return render(request, 'Gallery.html')


def Logout(request):
    return render(request, 'Logout.html')

