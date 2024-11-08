import django_filters
from django import forms
from django.contrib.admin.utils import lookup_field
from django.forms import CharField
from django_filters import CharFilter

from main_app.models import Receiver_request


class bloodFilter(django_filters.FilterSet):
    blood=CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'search blood group','class':'form-control'}))

    class Meta:
        model=Receiver_request
        fields=("blood",)