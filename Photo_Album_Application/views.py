from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'gallery.html')
    
def addPhoto(request):
    return render(request, 'add.html')
    
def login(request):
    return render(request, 'login.html')
    
def viewphoto(request):
    return render(request, 'photo.html')
    
def home(request):
    return render(request, 'home.html')