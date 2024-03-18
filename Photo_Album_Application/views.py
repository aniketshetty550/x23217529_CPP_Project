from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


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
    
def signup(request):
    return render(request, 'signup.html')
    
# def signup(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')

#         # Validate passwords
#         if password != password_confirm:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')  # Redirect back to signup page with error message

#         # Create new user
#         user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
#         user.save()

#         # Add success message
#         messages.success(request, "Account created successfully.")
        
#         # Redirect to login page
#         return redirect('login')  # Assuming you have a URL named 'login' defined in your URLconf
#     else:
#         # Render the signup form template
#         return render(request, 'signup.html')



# def signup(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')

#         # Validate passwords
#         if password != password_confirm:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')  # Redirect back to signup page with error message

#         # Create new user
#         try:
#             user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
#             user.save()
#             messages.success(request, "Account created successfully.")
#             return redirect('login')  # Redirect to login page after successful signup
#         except Exception as e:
#             messages.error(request, str(e))
#             return redirect('signup')  # Redirect back to signup page with error message
#     else:
#         # Render the signup form template
#         return render(request, 'signup.html')


# def login_view(request):
#     if request.method == 'POST':
#         # Assuming you have a custom user model with first_name, last_name, and password fields
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(request, first_name=first_name, last_name=last_name, password=password)
        
#         if user is not None:
#             # Log in the user
#             login(request, user)
#             # Redirect to the gallery page
#             return redirect('/gallery')
#         else:
#             # Invalid login, render login page with alert
#             return render(request, 'login.html', {'alert': True})
#     else:
#         # GET request, render login page
#         return render(request, 'login.html')
