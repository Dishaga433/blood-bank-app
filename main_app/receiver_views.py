from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import render, redirect

from main_app.forms import R_request, Fdbk, ReceiverRegister
from main_app.models import Receiver, Receiver_request, Feedback

@login_required(login_url='login_view')
def receiver_view(request):
    return render(request,"receiver/receiver_base.html")




@login_required(login_url='login_view')
def Receiever_req(request):
    data=R_request()
    user1=request.user
    print(user1)
    rcvr=Receiver.objects.get(user=user1)
    print(rcvr.id)
    if request.method == "POST":
        rname = R_request(request.POST)
        if rname.is_valid():
            obj=rname.save(commit=False)
            obj.Receiver_name=rcvr
            obj.save()
    return render(request,"receiver/request.html",{"form":data})




@login_required(login_url='login_view')
def req_table(request):
    user1 = request.user
    data = Receiver.objects.get(user=user1)
    data2=Receiver_request.objects.filter(Receiver_name=data)
    return render(request, "receiver/table_req.html", {'data': data2})


@login_required(login_url='login_view')
def rmv(request, id):   #request delete aakkan
    data = Receiver_request.objects.get(id=id)
    data.delete()
    return redirect("req_table")

@login_required(login_url='login_view')
def feedbk(request):
    data = Fdbk()
    user1=request.user
    rcvr = Receiver.objects.get(user=user1)

    if request.method == "POST":
        rname = Fdbk(request.POST)
        if rname.is_valid():
            obj = rname.save(commit=False)
            obj.receiver_name= rcvr
            obj.save()

    return render(request,"receiver/feedback.html",{"data":data})




@login_required(login_url='login_view')
def reply(request):
    user1=request.user
    data=Receiver.objects.get(user=user1)
    obj=Feedback.objects.filter(receiver_name=data)
    return render(request,"receiver/reply.html",{"data":obj})


@login_required(login_url='login_view')
def profile_receiver(request):
    user1 = request.user
    data = Receiver.objects.get(user=user1)
    return render(request,"receiver/profile_receiver.html",{"form":data})


@login_required(login_url='login_view')
def receiver_update(request, id):
    data = Receiver.objects.get(id=id)
    form = ReceiverRegister(instance=data)
    if request.method == "POST":
        profile = ReceiverRegister(request.POST,request.FILES, instance=data)
        if profile.is_valid():
            profile.save()
        return redirect("profile_receiver")
    return render(request, "receiver/profile_update.html", {"form": form})



def logou(request):
    logout(request)
    return redirect("/")