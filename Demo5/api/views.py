from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .auth import LoginView




"""curd opration api"""
class Studentapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    authentication_classes = []
    permission_classes = [IsAuthenticated]
