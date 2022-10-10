from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User


# Create your views here.
def home_view(request, *args, **kwargs):
  return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
  return render(request, "login.html", {})

def forget_password_view(request, *args, **kwargs):
  return render(request, "password.html",{})

def register_view(request, *args, **kwargs):
  return render(request, "register.html",{})

def dashboard_view(request, *args, **kwargs):
  return render(request, "home.html",{})

def tree_view(request, *args, **kwargs):
  return render(request, "home.html",{})



def HomePage(request):
  if request.method == "POST":
    FirstName = request.POST.get("firstName")
    LastName = request.POST.get("lastName")
    Email =  request.POST.get("email")
    Password1 = request.POST.get("password1")

    new_user = User.objects.create_user(FirstName,email,Password1)
    print("HIHIHIHI")
    new_user.first_name = Firstname
    new_user.last_name = LastName

    new_user.save() 


  return render(request,"register.html",{})