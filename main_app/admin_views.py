from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import request
from pyexpat.errors import messages

from main_app.forms import DonorRegister, ReceiverRegister, Fdbk
from main_app.models import Login, Donor, Receiver, Receiver_request, Feedback
from main_app.receiver_views import reply

@login_required(login_url='login_view')
def admin_view(request):
    return render(request,"admin/admin_base.html")


@login_required(login_url='login_view')
def table(request):
    data = Donor.objects.all()
    return render(request, "admin/table.html", {'data': data})


@login_required(login_url='login_view')
def remove(request,id):
    data=Donor.objects.get(id=id)
    data.delete()
    return redirect("admin_view")


@login_required(login_url='login_view')
def update(request, id):
    data = Donor.objects.get(id=id)
    form = DonorRegister(instance=data)
    if request.method == "POST":
        blood = DonorRegister(request.POST, instance=data)
        if blood.is_valid():
            blood.save()
        return redirect("admin_view")
    return render(request, "admin/update.html", {"form": form})




@login_required(login_url='login_view')
def table2(request):
    data = Receiver.objects.all()
    return render(request, "admin/table2.html", {'data': data})


@login_required(login_url='login_view')
def remove2(request,id):
    data=Receiver.objects.get(id=id)
    data.delete()
    return redirect("admin_view")


@login_required(login_url='login_view')
def update2(request, id):
    data = Receiver.objects.get(id=id)
    form = ReceiverRegister(instance=data)
    if request.method == "POST":
        blood2 = ReceiverRegister(request.POST, instance=data)
        if blood2.is_valid():
            blood2.save()
        return redirect("admin_view")
    return render(request, "admin/update2.html", {"form": form})


@login_required(login_url='login_view')
def req_admin(request):
    data2=Receiver_request.objects.all()
    return render(request, "admin/table_req.html", {'data': data2})


@login_required(login_url='login_view')
def donor_accept(request):
    obj=Receiver_request.objects.filter(status=1)
    return render(request,"admin/donation_accept.html",{"data":obj})


@login_required(login_url='login_view')
def accept(request,id):
    obj=Receiver_request.objects.get(id=id)
    obj.status = 2
    obj.save()
    return redirect('donor_accept')


@login_required(login_url='login_view')
def reject(request,id):
    obj=Receiver_request.objects.get(id=id)
    obj.status = 0
    obj.save()
    return redirect('donor_accept')


@login_required(login_url='login_view')
def accept_view(request):
    data=Receiver_request.objects.filter(status=2)
    return render(request,"admin/accept.html",{"data":data})



@login_required(login_url='login_view')
def reply_view(request):
    data=Feedback.objects.all()
    return render(request,"admin/admin_reply.html",{"data":data})


@login_required(login_url='login_view')
def reply_feedback(request,id):
    feedback=Feedback.objects.get(id=id)
    if request.method == "POST":
        r=request.POST.get('reply')
        feedback.reply=r
        feedback.save()
        # messages.info(request,'Reply send')

        return redirect('reply_view')
    return render(request,"admin/reply_feed.html",{"feedback":feedback})


def logou(request):
    logout(request)
    return redirect("/")