from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def prueba(request):
    return render(request,'prueba.html')