from django.urls import path
from . import views


urlpatterns =[
    
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('gallery/', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('logout/', views.logoutUser, name="logout"),
    path('deletePhoto/<str:pk>/', views.deletePhoto, name="deletePhoto"),
 ]   