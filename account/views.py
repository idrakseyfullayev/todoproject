from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import Account
from django.contrib.auth import authenticate, login, logout



class RegisterView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.info(request, "Please enter username")

        if not password:
            messages.info(request, "Please, enter password")

        if username and password:
            if User.objects.filter(username = username):
                messages.info(request, "Please, enter another username")
            elif password.isdigit():
                messages.info(request, "password must consist of letters and numbers or symbols")
            else:        
                user =User.objects.create_user(
                    username=username,
                    password=password)
            
                Account.objects.create(user=user)
                messages.success(request, "User Created")
                return redirect("todo:index")
                
                

        return redirect('account:register')    


class LoginView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request, user)
             return redirect("todo:index")
      
        else:
            messages.info(request, "user was not found")
            return redirect('account:login')
            
            
            
class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('todo:index')        



    





    


