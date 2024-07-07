from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login_page")
def receipes(request):
    print('aa')
    if request.method =="POST":
        data=request.POST
        ri=request.FILES.get('receipe_image')
        rn=data.get('receipe_name')
        rd=data.get('receipe_description')
        Reciepe.objects.create(receipe_name=rn,receipe_description=rd,receipe_image=ri)
        return redirect('/receipes')
    queryset = Reciepe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'receipes' : queryset}
    
    return render(request,'receipes.html',context)
def delete_receipe(request, id):
    queryset=Reciepe.objects.get(id =id)
    queryset.delete()
    return redirect('/receipes')

def update_receipe(request, id):
    queryset=Reciepe.objects.get(id=id)
    if request.method =="POST":
        data=request.POST
        ri=request.FILES.get('receipe_image')
        rn=data.get('receipe_name')
        rd=data.get('receipe_description') 
        queryset.receipe_name=rn
        queryset.receipe_description=rd
        if ri:
            queryset.receipe_image=ri
        queryset.save()
        return redirect('/receipes/')

    context={'receipes':queryset}
    return render(request,'update_receipes.html',context)
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login_page/')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login_page/')
        else:
            login(request,user)#to maintain user session
            return redirect('/receipes/')
        
    return render(request,"login.html")
def logout_page(request):
    logout(request)
    return redirect('/login_page/')
def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('Username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists')
            return redirect('/register/')
        user=User.objects.create(first_name=first_name,last_name=last_name,username=username,)
        user.set_password(password)
        user.save()
        messages.info(request,'User added successfully')
        return redirect('/register/')
    return render(request,'register.html')

