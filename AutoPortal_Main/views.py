from django.shortcuts import render


def home(request):
<<<<<<< HEAD
    return render(request,'home/home.html',{})

def prueba(request):
    return render(request,'prueba.html')


=======
    return render(request,'/home.html')
>>>>>>> 76d0e5b66bce37300933d08126039cc021c91f5c
