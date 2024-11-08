from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Login, Donor, Receiver, Receiver_request, Feedback


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username","password")


class DonorRegister(forms.ModelForm):
    class Meta:
        model = Donor
        fields ="__all__"
        exclude = ("user",)




class ReceiverRegister(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = "__all__"
        exclude = ("user",)



class DateInput(forms.DateInput):
    input_type = 'date'


class R_request(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Receiver_request
        fields = "__all__"
        exclude = ("Receiver_name","status","Donor_name",)



class Fdbk(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
        exclude=("date","reply","receiver_name",)


