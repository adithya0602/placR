from django.contrib import messages
from django.db import models
from django.shortcuts import render,redirect
from hello.models import Recruiter, Student
from django.contrib.auth import get_user_model
User=get_user_model()

from django.contrib.auth import authenticate, login
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def companies_visited(request):
    return render(request,"company.html")
def student_login(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        pass1=request.POST.get('pass1')
        user=authenticate(username=sname,password=pass1)
        if user is not None and user.is_student:
            login(request,user)
            messages.success(request,"successfully logged in")
            return render(request,"main.html")
        else:
            messages.error(request,"invalid credentials")
            return redirect("student_login")
    return render(request,"student_login.html")
def recruiter_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None and user.is_recruiter:
            login(request,user)
            messages.success(request,"successfully logged in")
            return render(request,"main.html")
        else:
            messages.error(request,"invalid credentials")
            return redirect("recruiter_login")
    return render(request,"recruiter.html")
def contact(request):
    return render(request,"contact.html")
def placed(request):
    return render(request,"placed.html")
def recruiter(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        idno=request.POST.get('idno')
        email=request.POST.get('email')
        cname=request.POST.get('cname')
        password=request.POST.get('password')
        Rpassword=request.POST.get('Rpassword')
        myuser=Recruiter(username=username,fname=fname,lname=lname,idno=idno,email=email,cname=cname,password=password)
        myuser.save()
        en=User.objects.create_user(username=username,email=email,password=password)
        en.first_name=fname
        en.last_name=lname
        en.save()
        messages.success(request,"successfully registered....")
        return redirect('recruiter_login')
    return render(request,"recruiter_register.html")
def student(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        iname=request.POST.get('iname')
        pass1=request.POST.get('pass1')
        Rpass1=request.POST.get('Rpass1')
        myuser=Student(sname=sname,fname=fname,lname=lname,email=email,iname=iname,pass1=pass1)
        myuser.save()
        en=User.objects.create_user(username=sname,email=email,password=pass1)
        en.first_name=fname
        en.last_name=lname
        en.save()
        messages.success(request,"successfully registered....")
        return redirect('student_login')
    return render(request,"student_register.html")