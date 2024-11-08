

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    date=models.DateField()


class Login(AbstractUser):
    is_donor=models.BooleanField(default=False)
    is_receiver=models.BooleanField(default=False)

class Donor(models.Model):

    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Donor")
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    DOB=models.DateField()
    ph_no=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    blood_group = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
    )
    blood = models.CharField(max_length=3, choices=blood_group)
    document = models.FileField(upload_to='documents/')


class Receiver(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Receiver")
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    DOB = models.DateField()
    ph_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    blood_group = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
    )
    blood = models.CharField(max_length=3, choices=blood_group)
    document = models.FileField(upload_to='documents/')


class Receiver_request(models.Model):
    Receiver_name=models.ForeignKey('Receiver',on_delete=models.CASCADE)
    Donor_name=models.ForeignKey('Donor',on_delete=DO_NOTHING,blank=True,null=True)
    date=models.DateField()
    blood_group = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
    )
    blood = models.CharField(max_length=3, choices=blood_group)
    hospital=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    status=models.IntegerField(default=0)



class Feedback(models.Model):
    receiver_name=models.ForeignKey("Receiver",on_delete=models.CASCADE)
    message=models.TextField()
    date=models.DateTimeField(auto_now=True)
    reply=models.CharField(max_length=200,null=True,blank=True)