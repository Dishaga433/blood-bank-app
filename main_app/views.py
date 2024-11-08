from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect


from main_app.forms import LoginRegister, DonorRegister, ReceiverRegister, R_request
from main_app.models import Donor, Receiver


# Create your views here.

def dashboard(request):
    return render(request,"dashboard.html")

def Login(request):
    return render(request,"login.html")




def DonorR(request):
    form1 = LoginRegister()
    form2=DonorRegister()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=DonorRegister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_donor=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login_view")


    return render(request,"DonorRegister.html",{"form1":form1,"form2":form2})




def ReceiverR(request):
    form1 = LoginRegister()
    form2=ReceiverRegister()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=ReceiverRegister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_receiver=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login_view")


    return render(request,"ReceiverRegister.html",{"form1":form1,"form2":form2})



def index(request):
    return render(request,"index.html")

def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        print(username)
        print(password)

        user=authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            if user.is_staff:
                print("admin")
                return redirect("admin_view")

            elif user.is_donor:
                print("admin")
                return redirect("donor_view")

            elif user.is_receiver:
                print("admin")
                return redirect("receiver_view")

        else:
            messages.info(request,'invalid credentials')
    return render(request,"login.html")




