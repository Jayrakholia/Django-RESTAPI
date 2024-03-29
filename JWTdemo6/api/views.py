from django.shortcuts import render
from .models import Student
from .serializers import Studentserializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .auth import LoginView

"""allowany give access to all user
JWTAuthentication used for jwt based authentication.
We use Studentserializer for data structure.
We use Student model for user data access.
Isadminuser give permission to admins only
"""


"""curd opration api"""
class Studentapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

"""In the basic authentication we need to send the username and password for every request.
In the session authentication we will send username and password at initial request. 
Then from server response we get the session id which stores in browser and gonna use that for requests.
In the token authentication we will send username and password at initial request. 
Then from server response we get the token and gonna use that for requests."""