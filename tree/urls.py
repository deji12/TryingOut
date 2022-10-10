"""tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dashboard.views import home_view, login_view, forget_password_view, register_view,dashboard_view,tree_view,HomePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_view, name="home"),
    path("",home_view,name="home"),
    path("login.html/",login_view,name="logout"),
    path("index.html/",home_view,name="login"),
    path("index.html/",dashboard_view,name="dashboard"),
    path("index.html/",tree_view,name="tree"),
    path("forgot-password.html/",forget_password_view,name="forgetPW"),
    path("register.html/",register_view,name="registers"),
    path("registeredYourAccount/",HomePage,name="Reg")
    
    
   

]
