from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import *
from .serializers import *

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello</h1>')


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer
