
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST["username"]
        ename=request.POST["email"]
        pname=request.POST["password"]
        phname=request.POST["phonenumber"]
        gname=request.POST["gender"]
        user_data=User(Username=uname,Email=ename,Password=pname,Phonenumber=phname,Gender=gname)
        user_data.save()
    return render(request,'signup.html')
     
def getusers(request):
    users=User.objects.all()
    return render(request,'display.html',{'eventive':users})

def delete(request,userid):
    User.objects.get(id=userid).delete()
    return redirect('user_display')

def update(request,userid):
     if request.method=="POST":
        uname=request.POST["username"]
        ename=request.POST["email"]
        pname=request.POST["password"]
        phname=request.POST["phonenumber"]
        gname=request.POST["gender"]
        User.objects.filter(id=userid).update(Username=uname,Email=ename,Password=pname,Phonenumber=phname,Gender=gname)
        return redirect('user_display')
     else:
        userdata=User.objects.get(id=userid)
        return render(request,'updateuser.html',{'usersdata':userdata})


def about(request):
   
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user_login=User.objects.get(Username=username,Password=password)
            request.session['user_id']=user_login.id
            return redirect('user_user')
        except User.DoesNotExist:
            return render(request,'login.html',{'message':'login failed'})
    return render(request,'login.html')

def user(request):
    if 'user_id' in request.session:
        use_id=request.session['user_id']
        userrdata=User.objects.get(id=use_id)
        render(request,'user.html')
    return render(request,'user_login')



    

def userhome(request):
    return render(request, 'user_userhome.html')

def birthday1(request):
    return render(request, 'simplebday.html')

def wedding(request):
    return render(request, 'wedding.html')


def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def logout(request):
    return render(request, 'home.html')