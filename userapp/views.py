from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def userregister(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        lname=req.POST.get('name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username alredy exists")
                return redirect('auth:userregister')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email alredy exists")
                return redirect('auth:userregister')
            
            else: 
                user=User.objects.create_user(first_name=name,last_name=lname,email=email,username=username,password=password)
                user.save()
                return redirect('home')
        else:
            messages.info(req,"password not matched")
            return redirect('auth:userregister')
    return render(req,'userregister.html')


def login(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(req,user)
            return redirect("home")
        else:
            messages.info(req,"invalidcredentials")
            return redirect("auth:login")
    return render(req,'login.html')

def logout(req):
    auth.logout(req)
    return redirect('home')