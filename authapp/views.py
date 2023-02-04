from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def Signup(request):
    if request.method=='POST':
        getEmail=request.POST.get('email')
        getPassword=request.POST.get('pass1')
        getConfirmPassword=request.POST.get('pass2')
        # print(getEmail,getPassword,getConfirmPassword)
        if getPassword!=getConfirmPassword:
            messages.info(request,"Password is dosn't match")
            return redirect ('/authapp/signup')
        
        try:
            if User.objects.get(username=getEmail):
                messages.warning(request,'Email is alredy taken')
                return redirect ('/authapp/signup')
        except Exception as identifier :
            pass

        myuser=User.objects.create_user(getEmail,getEmail,getPassword)
        myuser.save()
        messages.success(request,'User is created please login')
        return redirect('/authapp/login')

    return render(request,'signup.html')

def handleLogin(request):
    if request.method=='POST':
        getEmail=request.POST.get('email')
        getPassword=request.POST.get('pass1')
        myuser=authenticate(username=getEmail,password=getPassword)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'login success')
            return redirect('/')
        else:
            messages.error(request,"Invalid crentials")
            return redirect('/authapp/login')
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'Logout success')
    return render(request,'login.html')

