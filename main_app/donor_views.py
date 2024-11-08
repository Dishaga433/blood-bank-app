from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.filter import bloodFilter
from main_app.forms import DonorRegister
from main_app.models import Receiver_request, Donor

@login_required(login_url='login_view')
def donor_view(request):
    return render(request,"donor/donor_base.html")

@login_required(login_url='login_view')
def req_donor(request):

    obj=Receiver_request.objects.all()
    bloodfilter = bloodFilter(request.GET, queryset=obj)
    data = bloodfilter.qs
    return render(request, "donor/all_req.html", {'data': data,"bloodfilter":bloodfilter})


@login_required(login_url='login_view')
def donate(request,id):
    obj2=Receiver_request.objects.get(id=id)
    user1=request.user
    data=Donor.objects.get(user=user1)
    obj2.Donor_name=data
    obj2.status = 1
    obj2.save()
    return redirect("req_donor")

@login_required(login_url='login_view')
def profile_donor(request):
    user1 = request.user
    data = Donor.objects.get(user=user1)
    return render(request,"donor/profile.html",{"form":data})


@login_required(login_url='login_view')
def donor_update(request, id):
    data = Donor.objects.get(id=id)
    form = DonorRegister(instance=data)
    if request.method == "POST":
        profile = DonorRegister(request.POST,request.FILES, instance=data)
        if profile.is_valid():
            profile.save()
        return redirect("profile_donor")
    return render(request, "donor/profile_update.html", {"form": form})


def logou(request):
    logout(request)
    return redirect("/")

