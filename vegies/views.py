from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('recipe_name')
        receipe_description=data.get('recipe_description')
        image=request.FILES.get('image')

        receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            image=image
        )
        
        return redirect('/receipes/')
    
    queryset=receipe.objects.all()
    context={'sample':queryset}
    return render(request,'receipes.html',context) 

def delete_receipe(request,id):
    
    el=receipe.objects.get(id=id)
    el.delete()
    return redirect('/receipes/')
    

def update_receipe(request,id):
    queryset=receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST

        receipe_name=data.get('recipe_name')
        receipe_description=data.get('recipe_description')
        image=request.FILES.get('image')


        queryset.receipe_name= receipe_name
        queryset.receipe_description=receipe_description

        if image:
            queryset.image=image
        
        queryset.save()
        return redirect('/receipes/')
    

    context={'lol':queryset}
    return render(request,'update_receipes.html',context)


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists:
            messages.info(request,'Invalid Username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return render('/receipes/')




    return render(request,'login.html')

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User Already Exists')
            return redirect('/register/')


        user=User.objects.create(
            username=username,
            last_name=last_name,
            first_name=first_name
        )

        messages.info(request,'Account created Successfully')
        user.set_password(password)
        user.save()

        return redirect('/register')
    
    return render(request,'register.html')