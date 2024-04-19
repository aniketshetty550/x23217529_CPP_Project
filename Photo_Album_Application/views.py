from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Category, Photo
from django.contrib.auth import login as auth_login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        photo = Photo.objects.get(id=id)
        new_description = request.POST.get('description')
        photo.description = new_description
        photo.save()
        return redirect('gallery')  
    else:
        
        pass
    
    
   
def gallery(request):
    user = request.user
    print(user, " gallery")
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)
    
    
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'add.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')
    
    
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})
    
def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    print(photo)
    photo.delete()
    return gallery(request) 
    
    
def signup(request):
    # messages.success(request,"Account created successfully.")
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('signup') 

        
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')  
        except Exception as e:
            messages.error(request, str(e))
            return redirect('signup')  
    else:
        
        return render(request, 'signup.html')
    
    
def login(request):
    if request.method == 'POST':
        # Assuming you have a custom user model with first_name, last_name, and password fields
        email = request.POST.get('email')
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        
        # Authenticate user
        # user = authenticate(request, first_name=first_name, last_name=last_name, password=password)
        user = authenticate(request, username=email, password=password)
        
        print(user, email, password)
        if user is None:
            messages.error(request, "User Credential Invalid.")
            return render(request, 'login.html')
        else:
            auth_login(request,user)
            # Redirect to the gallery page
            return redirect('/gallery')
        
        # if user is not None:
        #     # Log in the user
        #     login(request, user)
        #     # Redirect to the gallery page
        #     return redirect('/gallery')
        # else:
        #     # Invalid login, render login page with alert
        #     return render(request, 'login.html', {'alert': True})
    else:
        # GET request, render login page
        return render(request, 'login.html')
