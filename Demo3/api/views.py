from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.models import User
from api.serializer import UserSerializer


# Create your views here.
class RCUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UDRUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
